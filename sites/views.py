from django.shortcuts import render

# Create your views here.
def sites_home_view(request):
    return render(request, 'sites/home.html')