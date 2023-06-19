from django.urls import path
from .views import *

urlpatterns = [
    path('', income_list, name='income_list'),
    path('create/', income_create, name='income_create'),
    path('edit/<int:income_id>/', income_edit, name='income_edit'),
    path('delete/<int:income_id>/', income_delete, name='income_delete'),
    path('total/<int:year>/<int:month>/', calculate_total_income, name='calculate_total_income'),
]
