from django.contrib import admin
from .models import Goal

class GoalAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'amount', 'description')
    list_filter = ('user',)
    search_fields = ('name', 'user__username')
    readonly_fields = ('user',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Goal, GoalAdmin)
