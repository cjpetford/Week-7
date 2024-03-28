from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

from . import forms

def register(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome {username}, we're glad to have you! Sending you to login page")
            return redirect('user-login')
    else:
        form = forms.UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def logout_page(request):
    logout(request)
    return redirect('recipes.home')

@login_required()
def profile(request):
  return render(request, 'users/profile.html')

