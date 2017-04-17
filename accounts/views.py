from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .validate import AccountValidator

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
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        validator = AccountValidator(username, password1, password2, email)
        
        if validator.is_valid():
            user = User.objects.create_user(username=username, password=password1, email=email)
            login(request, user)
            return redirect('sites:home')
        else:
            return render(request, 'accounts/register.html', validator.get_error())
    
    return render(request, 'accounts/register.html')