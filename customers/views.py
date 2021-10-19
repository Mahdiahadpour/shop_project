from django.conf import settings
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView

from customers.forms import LoginForm, UserProfile
from .models import Customer


# Create your views here.


def my_logout(request):
    logout(request)
    return redirect('login')


def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('invalid login')
    return render(request, 'customers/login.html', {'form': form})


@login_required()
def user_profile(request):
    profile = Customer.objects.filter(id=request.user.id)
    return render(request, 'customers/profile.html', context={'profile': profile})


def edit_profile(request):
    if request.method == 'POST':
        form = UserProfile(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('profile')
    else:
        form = UserProfile(instance=request.user)
        return render(request, 'customers/profile-edit.html', {'form': form})

