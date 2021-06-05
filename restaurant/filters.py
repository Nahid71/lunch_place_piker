from django_filters import rest_framework as filters
from .models import Restaurant, FoodItem, FoodManus


class RestaurantFilter(filters.FilterSet):

    class Meta:
        model = Restaurant
        exclude = ('logo',)


class FoodItemFilter(filters.FilterSet):

    class Meta:
        model = FoodItem
        exclude = ('picture',)


class FoodManusFilter(filters.FilterSet):

    class Meta:
        model = FoodManus
        fields = '__all__'