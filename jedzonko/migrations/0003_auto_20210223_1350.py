# Generated by Django 3.1.7 on 2021-02-23 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0002_auto_20210222_1812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipeplan',
            old_name='day_name_id',
            new_name='day_name',
        ),
        migrations.RenameField(
            model_name='recipeplan',
            old_name='plan_id',
            new_name='plan',
        ),
        migrations.RenameField(
            model_name='recipeplan',
            old_name='recipe_id',
            new_name='recipe',
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
