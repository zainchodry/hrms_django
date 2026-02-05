from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeForm

def is_admin(user):
    return user.role == 'admin'

def is_manager(user):
    return user.role == 'manager'

@login_required
def employee_list(request):
    if is_admin(request.user):
        employees = Employee.objects.all()
    elif is_manager(request.user):
        employees = Employee.objects.filter(department__manager=request.user)
    else:
        employees = Employee.objects.filter(user=request.user)

    return render(request, 'employees/list.html', {'employees': employees})

@login_required
def employee_create(request):
    if not (is_admin(request.user) or is_manager(request.user)):
        return redirect('employee_list')

    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employees/form.html', {'form': form, 'title': 'Add Employee'})

@login_required
def employee_update(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    if request.user != emp.user and not (is_admin(request.user) or is_manager(request.user)):
        return redirect('employee_list')

    form = EmployeeForm(request.POST or None, instance=emp)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employees/form.html', {'form': form, 'title': 'Edit Employee'})

@login_required
def employee_delete(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    if not is_admin(request.user):
        return redirect('employee_list')
    
    emp.delete()
    return redirect('employee_list')