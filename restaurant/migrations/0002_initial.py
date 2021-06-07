# Generated by Django 3.2.4 on 2021-06-07 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='votes',
            name='employee',
            field=models.ManyToManyField(related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='votes',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r_votes', to='restaurant.restaurant'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='foodmanus',
            name='food_item',
            field=models.ManyToManyField(blank=True, related_name='item_manus', to='restaurant.FoodItem'),
        ),
        migrations.AddField(
            model_name='foodmanus',
            name='restaurants',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_manus', to='restaurant.restaurant'),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='restaurants',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_items', to='restaurant.restaurant'),
        ),
        migrations.AlterUniqueTogether(
            name='fooditem',
            unique_together={('restaurants', 'name')},
        ),
    ]
