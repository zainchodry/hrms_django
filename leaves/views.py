from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Leave
from .forms import LeaveForm
from employees.models import Employee

def is_manager(user):
    return user.role == 'manager'

@login_required
def my_leaves(request):
    emp = Employee.objects.get(user=request.user)
    leaves = Leave.objects.filter(employee=emp)
    return render(request, 'my_leaves.html', {'leaves': leaves})

@login_required
def apply_leave(request):
    emp = Employee.objects.get(user=request.user)
    form = LeaveForm(request.POST or None)
    if form.is_valid():
        leave = form.save(commit=False)
        leave.employee = emp
        leave.save()
        return redirect('my_leaves')
    return render(request, 'leaves_form.html', {'form': form})

@login_required
def manage_leaves(request):
    if not is_manager(request.user):
        return redirect('my_leaves')
    leaves = Leave.objects.filter(employee__department__manager=request.user)
    return render(request, 'manage_leaves.html', {'leaves': leaves})

@login_required
def approve_leave(request, pk):
    leave = get_object_or_404(Leave, pk=pk)
    if request.user.role in ['manager', 'admin']:
        leave.status = 'approved'
        leave.save()
    return redirect('manage_leaves')

@login_required
def reject_leave(request, pk):
    leave = get_object_or_404(Leave, pk=pk)
    if request.user.role in ['manager', 'admin']:
        leave.status = 'rejected'
        leave.save()
    return redirect('manage_leaves')
