from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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
            return render(request, 'accounts/login.html', {'error':'Invalid User'})
        
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
        password = request.POST['password']
        if username and password:
            try:
                user = User.objects.get(username=username)
                return render(request, 'accounts/register.html', {'error':'Username already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                return redirect('sites:home')
        else:
            return render(request, 'accounts/register.html', {'error':'Username and Password cannot be blank'})
    
    return render(request, 'accounts/register.html')