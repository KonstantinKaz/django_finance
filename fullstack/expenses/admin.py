from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('expense_id', 'user', 'category', 'date', 'amount', 'description')
    list_filter = ('user', 'category', 'date')
    search_fields = ('user__username', 'category__name', 'date', 'description')
