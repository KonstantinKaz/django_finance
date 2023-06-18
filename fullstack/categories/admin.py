from django.contrib import admin
from .models import ExpenseCategory, IncomeCategory

admin.site.register(ExpenseCategory)
admin.site.register(IncomeCategory)
