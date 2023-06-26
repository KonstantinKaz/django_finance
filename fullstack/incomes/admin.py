from django.contrib import admin
from django.forms import SelectMultiple
from .models import Income

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('income_id', 'user', 'get_category_names', 'date', 'amount', 'description')
    list_filter = ('user', 'categories', 'date')
    date_hierarchy = 'date'
    search_fields = ('user__username', 'categories__name', 'date', 'description')
    filter_horizontal = ('categories',)
    list_display_links = ('income_id', 'user', 'get_category_names', 'date', 'amount', 'description')
    raw_id_fields = ('user',)
    readonly_fields = ('income_id',)

    def get_category_names(self, obj):
        return ', '.join([category.name for category in obj.categories.all()])

    get_category_names.short_description = 'Categories'
