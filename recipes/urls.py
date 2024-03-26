from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('mainrecipes/', views.mainrecipes, name="recipes-mainrecipes"),
]