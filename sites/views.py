from django.shortcuts import render

# Create your views here.
def sites_home_view(request):
    return render(request, 'sites/home.html')


def sites_about_view(request):
    return render(request, 'sites/about.html')