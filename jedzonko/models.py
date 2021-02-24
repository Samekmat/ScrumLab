from django.db import models
from django.utils import timezone

class Recipe(models.Model):
    name = models.CharField(max_length=64, unique=True)
    ingredients = models.ManyToManyField("Ingridents")
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    preparation_time = models.IntegerField()
    votes = models.IntegerField(default=0)
    directions = models.TextField()

class Plan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    recipes = models.ManyToManyField(Recipe, through="Recipeplan")

class Dayname(models.Model):
    day_name = models.CharField(max_length=16)
    order = models.IntegerField(unique=True)

class Recipeplan(models.Model):
    meal_name = models.CharField(max_length=255)
    order = models.IntegerField()
    day_name = models.ForeignKey(Dayname, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class Page(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255)

class Ingridents(models.Model):
    name = models.CharField(max_length=72)
    portion = models.CharField(max_length=72)



