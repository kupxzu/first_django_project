from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


def is_admin(user):
    return user.is_staff

@login_required
def dashboard(request):
    if request.user.is_staff:
        return redirect('admin_dashboard')
    return redirect('user_dashboard')

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')

@login_required
def user_dashboard(request):
    return render(request, 'accounts/user_dashboard.html')

def is_admin(user):
    return user.is_staff

@login_required
def dashboard(request):
    if request.user.is_staff:
        return redirect('admin_dashboard')
    return redirect('user_dashboard')

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')

@login_required
def user_dashboard(request):
    return render(request, 'accounts/user_dashboard.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'account created successfully. you can now login.')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})
