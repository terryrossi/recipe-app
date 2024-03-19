from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Ingredient

# Create your views here.
class IngredientListView(ListView):           #class-based view
   model = Ingredient                        #specify model
   template_name = 'recipes/ingredients_home.html'    #specify template 

# def home(request):
#     return render(request, 'ingredients/ingredients_home.html')
