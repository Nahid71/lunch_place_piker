from django.urls import path
from . import views


urlpatterns = [
   path('restaurant/', views.RestaurantView.as_view(), name='restaurant'),
   path('restaurantModify/<pk>/', views.RestaurantRUDView.as_view(), name='restaurantmodify'),
   path('foodManues/', views.FoodManusView.as_view(), name='foodManues'),
   path('foodManuesModify/<pk>/', views.FoodManusRUDView.as_view(), name='foodManuesmodify'),
   path('foodItem/', views.FoodItemView.as_view(), name='foodItem'),
   path('foodItemModify/<pk>/', views.FoodItemRUDView.as_view(), name='foodItemmodify'),
   path('vote/', views.VoteView.as_view(), name='vote'),
]