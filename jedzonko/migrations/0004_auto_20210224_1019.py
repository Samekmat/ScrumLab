# Generated by Django 2.2.6 on 2021-02-24 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0003_auto_20210223_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingridents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=72)),
                ('portion', models.CharField(max_length=72)),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='jedzonko.Ingridents'),
        ),
    ]