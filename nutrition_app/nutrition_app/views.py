# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Successfully navigated to the homepage")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("Successfully navigated to the about page")
    return render(request, 'about.html')
