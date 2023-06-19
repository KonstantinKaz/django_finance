from django.contrib import admin
from .models import Income

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('income_id', 'user', 'category', 'date', 'amount', 'description')
    list_filter = ('user', 'category', 'date')
    search_fields = ('user__username', 'category__name', 'date', 'description')
