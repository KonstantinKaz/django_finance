from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Income
from .forms import IncomeForm
from django.db.models import Sum
from decimal import Decimal
import datetime


def calculate_total_income(year, month, user):
    incomes = Income.objects.filter(date__year=year, date__month=month, user=user)
    total_income = incomes.aggregate(Sum('amount'))['amount__sum'] or Decimal('0')
    return total_income


@login_required
def income_list(request):
    selected_year = request.GET.get('year')
    year = datetime.date.today().year
    month = datetime.date.today().month
    user = request.user

    if selected_year:
        incomes = Income.objects.filter(date__year=selected_year, user=user)
        total_income_sum = calculate_total_income(selected_year, month, user)
    else:
        incomes = Income.objects.filter(user=user)
        total_income_sum = calculate_total_income(year, month, user)

    income_years = Income.objects.filter(user=user).values('date__year').distinct().order_by('-date__year')

    context = {
        'incomes': incomes,
        'total_income_sum': total_income_sum,
        'selected_year': selected_year,
        'income_years': income_years,
    }

    return render(request, 'incomes/income_list.html', context)


def income_create(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            form.save_m2m()  # Сохранение связанных ManyToMany-полей
            return redirect('income_list')
    else:
        form = IncomeForm()

    context = {'form': form}
    return render(request, 'incomes/income_create.html', context)


def income_edit(request, income_id):
    income = get_object_or_404(Income, income_id=income_id)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('income_list')
    else:
        form = IncomeForm(instance=income)
    return render(request, 'incomes/income_edit.html', {'form': form})

def income_delete(request, income_id):
    income = get_object_or_404(Income, income_id=income_id)
    if request.method == 'POST':
        income.delete()
        return redirect('income_list')
    return render(request, 'incomes/income_delete.html', {'income': income})
