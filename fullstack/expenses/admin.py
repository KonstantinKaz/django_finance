from django.contrib import admin
from django.forms import SelectMultiple
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('expense_id', 'user', 'get_category_names', 'date', 'amount', 'description')
    list_filter = ('user', 'categories', 'date')
    date_hierarchy = 'date'
    search_fields = ('user__username', 'categories__name', 'date', 'description')
    filter_horizontal = ('categories',)  # Добавление фильтрации с помощью filter_horizontal
    list_display_links = ('expense_id', 'user', 'get_category_names', 'date', 'amount', 'description')
    raw_id_fields = ('user',)
    readonly_fields = ('expense_id',)

    def get_category_names(self, obj):
        return ', '.join([category.name for category in obj.categories.all()])

    get_category_names.short_description = 'Categories'

    @admin.display(description='Amount')
    def amount_display(self, obj):
        return f'${obj.amount}'

