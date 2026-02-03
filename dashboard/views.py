from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from employees.models import Employee
from departments.models import Department
from attendance.models import Attendance
from leaves.models import Leave
from payroll.models import Payroll
from django.utils import timezone

@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        return render(request, 'dashboard_denied.html')

    today = timezone.now().date()

    context = {
        "total_employees": Employee.objects.count(),
        "total_departments": Department.objects.count(),
        "today_attendance": Attendance.objects.filter(date=today).count(),
        "pending_leaves": Leave.objects.filter(status='pending').count(),
        "total_payroll": Payroll.objects.count(),
    }

    return render(request, 'admin_dashboard.html', context)
