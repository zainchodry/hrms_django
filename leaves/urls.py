from django.urls import path
from . import views

urlpatterns = [
    path('my/', views.my_leaves, name='my_leaves'),
    path('apply/', views.apply_leave, name='apply_leave'),
    path('manage/', views.manage_leaves, name='manage_leaves'),
    path('<int:pk>/approve/', views.approve_leave, name='approve_leave'),
    path('<int:pk>/reject/', views.reject_leave, name='reject_leave'),
]
