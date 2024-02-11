from django.shortcuts import get_list_or_404, get_object_or_404
from ...models import Recipe


class RecipeRepository():
    def get_all_availables(self):
        recipes = Recipe.objects.filter(
            is_published=True).order_by('-id')
        return recipes

    def get_all_availables_by_category(self, category_id):
        recipes = get_list_or_404(Recipe.objects.filter(
            category__id=category_id, is_published=True).order_by('-id'))

        return recipes

    def get_by_id(self, id):
        recipe = get_object_or_404(Recipe, pk=id, is_published=True)
        return recipe
