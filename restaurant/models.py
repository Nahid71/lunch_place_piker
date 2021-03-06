import uuid
from django.db import models

# Create your models here.
class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='restaurants')
    logo = models.FileField(upload_to='restaurant/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    picture = models.FileField(upload_to='food_item/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField(default=0)
    restaurants = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='food_items')
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.name} Restaurant: {self.restaurants.name}'
    
    class Meta:
        unique_together = ('restaurants', 'name')



class FoodManus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurants = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='food_manus')
    day = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    food_item = models.ManyToManyField(FoodItem, related_name='item_manus', blank=True)
    note = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.id)


class Votes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='r_votes')
    employee = models.ManyToManyField('user.CustomUser', related_name='votes')
    vote_count = models.PositiveIntegerField(default=0)
    day = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.id)


class Winner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, related_name='winner', null=True)
    day = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.id)
