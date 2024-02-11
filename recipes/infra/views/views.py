from django.shortcuts import render
from ..repositories.recipes import RecipeRepository


class RecipeView():
    def __init__(self, recipeRepository: RecipeRepository) -> None:
        self.recipeRepository = recipeRepository

    def home(self, request):
        recipes = self.recipeRepository.get_all_availables()
        return render(request, 'recipes/pages/home.html', context={
            'recipes': recipes
        })

    def category(self, request, category_id):
        recipes = self.recipeRepository.get_all_availables_by_category(
            category_id)
        return render(request, 'recipes/pages/category.html', context={
            'recipes': recipes,
            'category': f'{recipes[0].category.name} - Categoria |'
        })

    def recipe(self, request, id):
        recipe = self.recipeRepository.get_by_id(id)
        return render(request, 'recipes/pages/recipe-view.html', context={
            'recipe': recipe,
            'is_detail_page': True
        })
