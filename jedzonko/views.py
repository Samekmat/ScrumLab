from datetime import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
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
        latest_plan = Plan.objects.latest('created')
        days = [x.day_name.order for x in latest_plan.recipeplan_set.all()]
        days = set(days)
        counter = 0
        for recipe in recipes:
            counter += 1
        ctx = {
            'counter': counter, "plans_counter": plans_counter, "latest_plan": latest_plan,
            "days": days,
        }
        return render(request, "dashboard.html", ctx)


class RecipeDetailView(View):
    def get(self, request, id):
        return render(request, "app-recipe-details.html")


class RecipeListView(View):
    def get(self, request):
        recipe_list = Recipe.objects.order_by('-votes', '-created')
        paginator = Paginator(recipe_list, 50) # tu można zmienić liczbę przepisów ustawianych na stronie
        page = request.GET.get('page', 1)
        try:
            recipes = paginator.page(page)
        except PageNotAnInteger:
            recipes = paginator.page(1)
        except EmptyPage:
            recipes = paginator.page(paginator.num_pages)

        return render(request, "app-recipes.html", {'recipes': recipes})


class RecipeAddView(View):
    def get(self, request):
        return render(request, "app-add-recipe.html")
    def post(self, request):
        return render(request, "app-add-recipe.html")

class RecipeModifyView(View):
    def get(self, request, id):
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

    def post(self, request):
        name = request.POST.get('planName')
        description = request.POST.get('planDesc')

        if not name or not description:
            ctx = {'Error': 'Plan name, description or both are empty'}
            return render(request, "app-add-schedules.html", ctx)

        p = Plan()
        p.name = name
        p.description = description
        p.save()
        return redirect('plan_detail', id=p.id)


class PlanAddRecipeView(View):
    def get(self, request):
        return render(request, "app-schedules-meal-recipe.html")

