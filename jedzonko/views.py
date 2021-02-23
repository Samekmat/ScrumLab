from datetime import datetime

from django.shortcuts import render
from django.views import View
from jedzonko.models import Recipe, Plan, Dayname, Recipeplan, Page
import random


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)


class MainView(View):

    def get(self, request):
        results = Recipe.objects.all()
        results = [x for x in results]
        random.shuffle(results)
        results = results[:3]
        ctx = {'results': results}
        return render(request, 'index.html', ctx)


class DashboardView(View):
    def get(self, request):
        plans_counter = Plan.objects.all().count()
        recipes = Recipe.objects.all()
        counter = 0
        for recipe in recipes:
            counter += 1
        return render(request, "dashboard.html", {'counter': counter, "plans_counter": plans_counter})


class RecipeDetailView(View):
    def get(self, request):
        return render(request, "app-recipe-details.html")


class RecipeListView(View):
    def get(self, request):
        return render(request, "app-recipes.html")


class RecipeAddView(View):
    def get(self, request):
        return render(request, "app-add-recipe.html")
    def post(self, request):
        return render(request, "app-add-recipe.html")

class RecipeModifyView(View):
    def get(self, request):
        return render(request, "app-edit-recipe.html")


class PlanDetailView(View):
    def get(self, request):
        return render(request, "app-details-schedules.html")


class PlanListView(View):
    def get(self, request):
        return render(request, "app-schedules.html")


class PlanAddView(View):
    def get(self, request):
        return render(request, "app-add-schedules.html")


class PlanAddRecipeView(View):
    def get(self, request):
        return render(request, "app-schedules-meal-recipe.html")

