from django.conf import settings
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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


def index(request):
    return HttpResponse('~~~~~~hi~~~~~~')


def user_profile(request):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}next={request.path}")
    profile = Customer.objects.filter(id=request.user.id)
    return render(request, 'customers/profile.html', context={'profile': profile})


# def user_profile_edit(request):
#     if not request.user.is_authenticated:
#         return redirect(f"{settings.LOGIN_URL}next={request.path}")
#     form = UserProfile
#     if request.method == 'PUT':
#         form = UserProfile(request.PUT)
#         if form_is
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfile(request.POST, instance=request.user)
        # form1 = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            # form1.save()
            return redirect('profile')
    else:
        form = UserProfile(instance=request.user)
        # form1 = UpdateProfileForm(instance=request.user)

        return render(request, 'customers/profile-edit.html', {'form': form})

# def user_profile(request, pk):
#     user = get_object_or_404(Customer, pk=pk)
#     return render(request, 'profile.html', {'user': user})
