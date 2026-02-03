from django.urls import path
from . import views

urlpatterns = [
    path('', views.payroll_list, name='payroll_list'),
    path('generate/', views.generate_payroll, name='generate_payroll'),
]
