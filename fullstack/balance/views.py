from django.shortcuts import render
from django.db import models
from .models import Balance
from incomes.models import Income
from expenses.models import Expense


def calculate_balance(user):
    incomes_sum = Income.objects.filter(user=user).aggregate(total=models.Sum('amount'))['total'] or 0
    expenses_sum = Expense.objects.filter(user=user).aggregate(total=models.Sum('amount'))['total'] or 0
    total_balance = incomes_sum - expenses_sum

    balance, created = Balance.objects.get_or_create(user=user)
    balance.total_balance = total_balance
    balance.save()

def balance(request):
    user = request.user
    calculate_balance(user)

    balance = Balance.objects.get(user=user)
    return render(request, 'balance/balance.html', {'balance': balance})
