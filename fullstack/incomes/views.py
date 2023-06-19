from django.shortcuts import render, get_object_or_404, redirect
from .models import Income
from .forms import IncomeForm
from django.db.models import Sum
from decimal import Decimal
import datetime
from django.contrib.auth.models import User

# ...

def calculate_total_income(year, month):
    income = Income.objects.filter(date__year=year, date__month=month)
    total_income = income.aggregate(Sum('amount'))['amount__sum'] or Decimal('0')
    return total_income

def income_list(request):
    selected_year = request.GET.get('year')
    year = datetime.date.today().year
    month = 6  # Замените на нужный вам месяц
    if selected_year:
        incomes = Income.objects.filter(date__year=selected_year)
        total_income_sum = calculate_total_income(selected_year, month)
    else:
        incomes = Income.objects.all()
        total_income_sum = calculate_total_income(year, month)
    income_years = Income.objects.values('date__year').distinct().order_by('-date__year')

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
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('income_list')
    else:
        form = IncomeForm()
    return render(request, 'incomes/income_create.html', {'form': form})

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