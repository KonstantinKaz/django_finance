from django.shortcuts import render, get_object_or_404, redirect
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
from decimal import Decimal
import datetime
from django.contrib.auth.decorators import login_required

def calculate_total_expenses(year, month, user):
    expenses = Expense.objects.filter(date__year=year, date__month=month, user=user)
    total_expenses = expenses.aggregate(Sum('amount'))['amount__sum'] or Decimal('0')
    return total_expenses

@login_required
def expense_list(request):
    selected_year = request.GET.get('year')
    year = datetime.date.today().year
    month = datetime.date.today().month
    user = request.user

    if selected_year:
        expenses = Expense.objects.filter(date__year=selected_year, user=user)
        total_expenses_sum = calculate_total_expenses(selected_year, month, user)
    else:
        expenses = Expense.objects.filter(user=user)
        total_expenses_sum = calculate_total_expenses(year, month, user)

    expense_years = Expense.objects.filter(user=user).values('date__year').distinct().order_by('-date__year')

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



