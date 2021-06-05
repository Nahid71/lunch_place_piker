from rest_framework import serializers
from .models import Restaurant, FoodItem, FoodManus


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = '__all__'
    
    def to_representation(self, instance):
        request = self.context['request']
        data = super(RestaurantSerializer, self).to_representation(instance)
        data['logo'] = request.build_absolute_uri(instance.logo.url) if instance.logo else None
        return data


class FoodItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodItem
        fields = '__all__'
    
    def to_representation(self, instance):
        request = self.context['request']
        data = super(FoodItemSerializer, self).to_representation(instance)
        data['picture'] = request.build_absolute_uri(instance.picture.url) if instance.picture else None
        return data


class FoodManusSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodManus
        fields = '__all__'
    
    def to_representation(self, instance):
        request = self.context['request']
        data = {}
        data['id'] = instance.id
        data['restaurants'] = instance.restaurants.id
        data['day'] = instance.day
        data['note'] = instance.note
        data['food_item'] = FoodItemSerializer(instance.food_item.all(), many=True, context={"request": request})
        data['created'] = instance.created
        data['modified'] = instance.modified
        return data
