from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('expense_id', 'user', 'get_category_names', 'date', 'get_amount_display', 'description')
    list_filter = ('user', 'categories', 'date')
    date_hierarchy = 'date'
    search_fields = ('user__username', 'categories__name', 'date', 'description')
    filter_horizontal = ('categories',)
    list_display_links = ('expense_id', 'user', 'get_category_names', 'date', 'get_amount_display', 'description')
    raw_id_fields = ('user',)
    readonly_fields = ('expense_id',)

    def get_category_names(self, obj):
        return ', '.join([category.name for category in obj.categories.all()])

    get_category_names.short_description = 'Категория'

    def get_amount_display(self, obj):
        return obj.amount

    get_amount_display.short_description = 'Циферки'
