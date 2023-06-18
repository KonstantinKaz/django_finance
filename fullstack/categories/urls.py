# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', category_list, name='category_list'),
    path('expense/create/', expense_category_create, name='expense_category_create'),
    path('expense/<int:category_id>/update/', expense_category_update, name='expense_category_update'),
    path('expense/<int:category_id>/delete/', expense_category_delete, name='expense_category_delete'),
    path('income/create/', income_category_create, name='income_category_create'),
    path('income/<int:category_id>/update/', income_category_update, name='income_category_update'),
    path('income/<int:category_id>/delete/', income_category_delete, name='income_category_delete'),
]
