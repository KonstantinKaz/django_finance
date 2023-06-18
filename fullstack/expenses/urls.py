from django.urls import path
from .views import *

urlpatterns = [
    path('', expense_list, name='expense_list'),
    path('create/', expense_create, name='expense_create'),
    path('edit/<int:expense_id>/', expense_edit, name='expense_edit'),
    path('delete/<int:expense_id>/', expense_delete, name='expense_delete'),
    path('total/<int:year>/<int:month>/', calculate_total_expenses, name='calculate_total_expenses'),
]
