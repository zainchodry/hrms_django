from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Payroll
from .utils import calculate_deductions
from employees.models import Employee

@login_required
def generate_payroll(request):
    if request.user.role != 'admin':
        return redirect('employee_list')

    if request.method == 'POST':
        month = request.POST.get('month')
        employees = Employee.objects.all()

        for emp in employees:
            daily = emp.salary / 30
            deduction = calculate_deductions(emp, month, daily)
            net = emp.salary - deduction

            Payroll.objects.create(
                employee=emp,
                month=month,
                basic_salary=emp.salary,
                deductions=deduction,
                net_salary=net
            )
        return redirect('payroll_list')

    return render(request, 'payroll_generate.html')

@login_required
def payroll_list(request):
    if request.user.role == 'admin':
        payrolls = Payroll.objects.all()
    else:
        emp = Employee.objects.get(user=request.user)
        payrolls = Payroll.objects.filter(employee=emp)

    return render(request, 'payroll/list.html', {'payrolls': payrolls})
