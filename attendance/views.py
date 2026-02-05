from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Attendance
from employees.models import Employee

@login_required
def my_attendance(request):
    emp = Employee.objects.get(user=request.user)
    records = Attendance.objects.filter(employee=emp).order_by('-date')
    today = timezone.now().date()
    today_record = Attendance.objects.filter(employee=emp, date=today).first()
    return render(request, 'attendance/list.html', {'records': records, 'today_record': today_record})

@login_required
def check_in(request):
    emp = Employee.objects.get(user=request.user)
    today = timezone.now().date()
    att, created = Attendance.objects.get_or_create(employee=emp, date=today)
    if not att.check_in:
        att.check_in = timezone.now().time()
        if att.check_in.hour > 9:
            att.is_late = True
        att.save()
    return redirect('my_attendance')

@login_required
def check_out(request):
    emp = Employee.objects.get(user=request.user)
    today = timezone.now().date()
    att = Attendance.objects.get(employee=emp, date=today)
    if not att.check_out:
        att.check_out = timezone.now().time()
        att.save()
    return redirect('my_attendance')
