from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Department
from .forms import DepartmentForm

def is_admin_or_manager(user):
    return user.role in ['admin', 'manager']

@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'list.html', {'departments': departments})

@login_required
def department_create(request):
    if not is_admin_or_manager(request.user):
        return redirect('department_list')

    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('department_list')
    return render(request, 'department_form.html', {'form': form})

@login_required
def department_update(request, pk):
    dept = get_object_or_404(Department, pk=pk)
    if not is_admin_or_manager(request.user):
        return redirect('department_list')

    form = DepartmentForm(request.POST or None, instance=dept)
    if form.is_valid():
        form.save()
        return redirect('department_list')
    return render(request, 'departments_form.html', {'form': form})

@login_required
def department_delete(request, pk):
    dept = get_object_or_404(Department, pk=pk)
    if request.user.role == 'admin':
        dept.delete()
    return redirect('department_list')
