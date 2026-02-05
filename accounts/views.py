from django.shortcuts import render, redirect
from . models import *
from . forms import *
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from . forms import LoginForm
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user

        if user.role == 'admin':
            messages.success(self.request, f"Welcome Back Admin {user.username}! 👋")
            return reverse_lazy('admin_dashboard')
        elif user.role == 'manager':
            messages.success(self.request, f"Welcome Back Manager {user.username}! 👋")
            return reverse_lazy('manager_dashboard')
        
        elif user.role == 'staff':
            messages.success(self.request, f"Welcome Back {user.username}! 👋")
            return reverse_lazy('staff_dashboard')
        
        else:
            messages.success(self.request, f"Please Select a Role first")
            return reverse_lazy('login')

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)

@login_required
def profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    context = {'form': form}
    return render(request, 'profile.html', context)

def logout(request):
    auth_logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')
