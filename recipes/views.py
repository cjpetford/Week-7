from django.shortcuts import render, HttpResponse

recipes = [

    {
    'author': 'Connor',
    'title': 'Homemade Lasagne',
    'ingredients': 'everything we need to make it',
    'method': 'how to make it',
    'date_posted': 'March 26, 2024'
    },

    {
    'author': 'Jamie',
    'title': 'Italian Pasta',
    'ingredients': 'everything we need to make it',
    'method': 'how to make it',
    'date_posted': 'March 27, 2024'
    },

    {
    'author': 'Mia',
    'title': 'Sliders',
    'ingredients': 'everything we need to make it',
    'method': 'how to make it',
    'date_posted': 'March 28, 2024'
    },

]

# Create your views here.

def home(request):
    context={
        'recipes' : recipes
    }
    return render(request, "recipes/home.html", context)

def mainrecipes(request):
    return render(request, "recipes/mainrecipes.html", {'title':'Main Recipes'})
