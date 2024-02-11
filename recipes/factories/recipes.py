from ..infra.repositories.recipes import RecipeRepository
from ..infra.views.views import RecipeView


class MakeRecipe():

    @staticmethod
    def getInstance():
        recipeRepository = RecipeRepository()
        recipeView = RecipeView(recipeRepository)
        return recipeView
