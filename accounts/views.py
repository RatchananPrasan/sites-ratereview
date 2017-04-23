from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import RegisterForm, Profile

# Create your views here.
def accounts_login_view(request):
    if request.user.is_authenticated:
        return redirect('sites:home')
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sites:home')
        else:
            return render(request, 'accounts/login.html', {'error':'Invalid Username or Password.'})
        
    return render(request, 'accounts/login.html')


def accounts_logout_view(request):
    if request.method == "POST":
        logout(request)
        
    return redirect('sites:home')

def accounts_register_view(request):
    if request.user.is_authenticated:
        return redirect('sites:home')
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user = User.objects.create(username=username, password=password, email=email)
            user.set_password(password)
            user.save()
            profile = Profile.objects.create(user=user)
            login(request, user)
            return redirect('sites:home')
    else:
        form = RegisterForm()
        
    return render(request, 'accounts/register.html', {'form':form})