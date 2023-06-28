from django.contrib import admin
from .models import Balance

@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('balance_id', 'user', 'total_balance')
    list_filter = ('user',)
    search_fields = ('user__username',)
    readonly_fields = ('balance_id', 'user')
