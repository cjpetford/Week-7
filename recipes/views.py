from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.

def home(request):
    recipes = models.Recipe.objects.all()
    context={
        'recipes' : recipes
    }
    return render(request, "recipes/home.html", context)

def mainrecipes(request):
    return render(request, "recipes/mainrecipes.html", {'title':'Main Recipes'})
