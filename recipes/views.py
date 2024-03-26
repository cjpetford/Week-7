from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Seasonique - Original recipes all year round!</h1>")

def mainrecipes(request):
    return HttpResponse("<h1>Seasonique</h1>")