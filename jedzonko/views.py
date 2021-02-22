from datetime import datetime

from django.shortcuts import render
from django.views import View
from jedzonko.models import Recipe

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
        recipes = Recipe.objects.all()
        counter = 0
        for recipe in recipes:
            counter += 1
        return render(request, "dashboard.html", {'counter': counter})

