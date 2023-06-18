from django.shortcuts import render, get_object_or_404, redirect
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum

import datetime

def expense_list(request):
    expenses = Expense.objects.all()
    year = datetime.date.today().year
    month = 6  # Замените на ваше значение месяца
    total_expenses = calculate_total_expenses(year, month)

    context = {
        'expenses': expenses,
        'total_expenses': total_expenses,
    }

    return render(request, 'expenses/expense_list.html', context)


def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_create.html', {'form': form})


def expense_edit(request, expense_id):
    expense = get_object_or_404(Expense, expense_id=expense_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
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


def calculate_total_expenses(year, month):
    total_expenses = Expense.objects.filter(date__year=year, date__month=month).aggregate(Sum('amount'))
    return total_expenses
