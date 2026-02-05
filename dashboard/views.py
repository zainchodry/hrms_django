from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        messages.error(request, "Access denied. Admin rights required.")
        return redirect_to_role_dashboard(request.user)
    return render(request, 'dashboard/admin_dashboard.html')

@login_required
def manager_dashboard(request):
    if request.user.role != 'manager':
        messages.error(request, "Access denied. Manager rights required.")
        return redirect_to_role_dashboard(request.user)
    return render(request, 'dashboard/manager_dashboard.html')

@login_required
def staff_dashboard(request):
    if request.user.role != 'staff':
        messages.error(request, "Access denied. Staff rights required.")
        return redirect_to_role_dashboard(request.user)
    return render(request, 'dashboard/staff_dashboard.html')

def redirect_to_role_dashboard(user):
    """Helper to redirect user to their correct dashboard."""
    if user.role == 'admin':
        return redirect('admin_dashboard')
    elif user.role == 'manager':
        return redirect('manager_dashboard')
    elif user.role == 'staff':
        return redirect('staff_dashboard')
    return redirect('profile')
