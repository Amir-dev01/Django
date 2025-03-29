from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views import View
from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe_list')


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipe_list')


class IngredientAddView(View):
    def get(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        form = IngredientForm()
        return render(request, 'recipes/ingredient_form.html', {'form': form, 'recipe': recipe})

    def post(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
            return redirect('recipe_detail', pk=recipe.id)
        return render(request, 'recipes/ingredient_form.html', {'form': form, 'recipe': recipe})
