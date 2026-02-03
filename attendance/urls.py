from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.my_attendance, name='my_attendance'),
    path('check-in/', views.check_in, name='check_in'),
    path('check-out/', views.check_out, name='check_out'),
]
