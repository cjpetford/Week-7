from django.urls import path
from . import views

'app/model_viewtype'
'recipes/recipe_detail.html'

urlpatterns = [
    path('', views.RecipeListView.as_view(), name="recipes-home"),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name="recipes-detail"),
    path('recipes/create/', views.RecipeCreateView.as_view(), name="recipes-create"),
    path('recipes/<int:pk>/update', views.RecipeUpdateView.as_view(), name="recipes-update"),
    path('recipes/<int:pk>/delete', views.RecipeDeleteView.as_view(), name="recipes-delete"),
    path('mainrecipes/', views.mainrecipes, name="recipes-mainrecipes"),
]