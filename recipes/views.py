from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipes_home.html'


class RecipeDetailView(LoginRequiredMixin, DetailView): #class-based “protected” view
    model = Recipe
    template_name = 'recipes/recipe_detail.html'