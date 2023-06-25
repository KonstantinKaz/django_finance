from django.shortcuts import render, get_object_or_404, redirect
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
from decimal import Decimal
import datetime
from django.contrib.auth.models import User


# ...

def calculate_total_expenses(year, month):
    expenses = Expense.objects.filter(date__year=year, date__month=month)
    total_expenses = expenses.aggregate(Sum('amount'))['amount__sum'] or Decimal('0')
    return total_expenses


def expense_list(request):
    selected_year = request.GET.get('year')
    year = datetime.date.today().year
    month = 6  # Замените на нужный вам месяц
    if selected_year:
        expenses = Expense.objects.filter(date__year=selected_year)
        total_expenses_sum = calculate_total_expenses(selected_year, month)
    else:
        expenses = Expense.objects.all()
        total_expenses_sum = calculate_total_expenses(year, month)
    expense_years = Expense.objects.values('date__year').distinct().order_by('-date__year')

    context = {
        'expenses': expenses,
        'total_expenses_sum': total_expenses_sum,
        'selected_year': selected_year,
        'expense_years': expense_years,
    }

    return render(request, 'expenses/expense_list.html', context)


def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            form.save_m2m()  # Сохранение связанных ManyToMany-полей
            return redirect('expense_list')
    else:
        form = ExpenseForm()

    context = {'form': form}
    return render(request, 'expenses/expense_create.html', context)


def expense_edit(request, expense_id):
    expense = get_object_or_404(Expense, expense_id=expense_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/expense_edit.html', {'form': form})



def expense_delete(request, expense_id):
    expense = get_object_or_404(Expense, expense_id=expense_id)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expenses/expense_delete.html', {'expense': expense})



