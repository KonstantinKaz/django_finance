from django.db import models
from django.contrib import admin
from django.forms import SelectMultiple
from .models import Income

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('income_id', 'user', 'get_category_names', 'date', 'amount', 'description')
    list_filter = ('user', 'categories', 'date')
    search_fields = ('user__username', 'categories__name', 'date', 'description')
    formfield_overrides = {
        models.ManyToManyField: {'widget': SelectMultiple},
    }

    def get_category_names(self, obj):
        return ', '.join([category.name for category in obj.categories.all()])

    get_category_names.short_description = 'Categories'
