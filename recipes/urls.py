from django.urls import path
from .factories.recipes import MakeRecipe

app_name = 'recipes'
recipe = MakeRecipe().getInstance()

urlpatterns = [
    path('', recipe.home, name="home"),
    path('recipes/category/<int:category_id>/',
         recipe.category, name="category"),
    path('recipes/<int:id>/', recipe.recipe, name="recipe"),
]
