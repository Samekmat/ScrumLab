from datetime import datetime

from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        # x =5
        return render(request, "test.html", ctx)


class MainView(View):

    def get(self, request):
        return render(request, "index.html")


class DashboardView(View):
    def get(self, request):
        return render(request, "dashboard.html")


class RecipeDetailView(View):
    def get(self, request):
        return render(request, "app-recipe-details.html")


class RecipeListView(View):
    def get(self, request):
        return render(request, "app-recipes.html")


class RecipeAddView(View):
    def get(self, request):
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
