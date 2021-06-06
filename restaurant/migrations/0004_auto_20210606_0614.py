# Generated by Django 3.2.4 on 2021-06-06 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20210605_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='votes',
            name='vote_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='foodmanus',
            name='food_item',
            field=models.ManyToManyField(blank=True, related_name='item_manus', to='restaurant.FoodItem'),
        ),
    ]
