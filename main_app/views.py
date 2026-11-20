from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def find_us_view(request):
    return render(request, 'find_us.html')

def concerts_view(request):
    return render(request, 'concerts.html')

def orchestra_view(request):
    return render(request, 'orchestra.html')
# Create your views here.
