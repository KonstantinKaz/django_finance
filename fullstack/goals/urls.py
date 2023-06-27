from django.urls import path
from .views import *


urlpatterns = [
    path('', goal_list, name='goal_list'),
    path('create/', goal_create, name='goal_create'),
    path('<int:goal_id>/update/', goal_update, name='goal_update'),
    path('<int:goal_id>/delete/', goal_delete, name='goal_delete'),
]
