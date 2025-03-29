from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeDeleteView, IngredientAddView


urlpatterns = [
    path('recipe/list/', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/create/', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),
    path('recipe/<int:recipe_id>/add_ingredient/', IngredientAddView.as_view(), name='ingredient_add'),
]
