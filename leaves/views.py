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
    leaves = Leave.objects.filter(employee=emp).order_by('-start_date')
    return render(request, 'leaves/my_leaves.html', {'leaves': leaves})

@login_required
def apply_leave(request):
    emp = Employee.objects.get(user=request.user)
    form = LeaveForm(request.POST or None)
    if form.is_valid():
        leave = form.save(commit=False)
        leave.employee = emp
        leave.save()
        return redirect('my_leaves')
    return render(request, 'leaves/form.html', {'form': form, 'title': 'Apply for Leave'})

@login_required
def manage_leaves(request):
    if not (request.user.role == 'manager' or request.user.role == 'admin'):
        return redirect('my_leaves')
    
    if request.user.role == 'manager':
        leaves = Leave.objects.filter(employee__department__manager=request.user).order_by('-created_at')
    else:
        leaves = Leave.objects.all().order_by('-created_at')

    return render(request, 'leaves/manage_leaves.html', {'leaves': leaves})

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
