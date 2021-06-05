from django.contrib import admin
from .models import FoodItem, Restaurant, FoodManus, Votes, Winner
# Register your models here.

admin.site.register(FoodItem)
admin.site.register(Restaurant)
admin.site.register(FoodManus)
admin.site.register(Votes)
admin.site.register(Winner)
