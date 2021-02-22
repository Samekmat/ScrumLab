from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=64, unique=True)
    ingredients = models.TextField()
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    preparation_time = models.IntegerField()
    votes = models.IntegerField(default=0)




