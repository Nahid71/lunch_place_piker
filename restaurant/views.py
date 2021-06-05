from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from datetime import datetime, timedelta
from .models import Restaurant, FoodItem, FoodManus, Votes
from restaurant_picker.pagination import DisplaySize
from .serializers import RestaurantSerializer, FoodItemSerializer, FoodManusSerializer, VotesSerializer
from .filters import RestaurantFilter, FoodItemFilter, FoodManusFilter


class RestaurantView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    pagination_class = DisplaySize
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_class = RestaurantFilter


class RestaurantRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return Restaurant.objects.none()

        idx = self.kwargs['pk']
        # only the Restaurant owner or profile_manager (role) can change details
        return Restaurant.objects.filter(id=idx)


class FoodItemView(generics.ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    pagination_class = DisplaySize
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_class = FoodItemFilter


class FoodItemRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FoodItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return FoodItem.objects.none()

        idx = self.kwargs['pk']
        # only the FoodItem owner or profile_manager (role) can change details
        return FoodItem.objects.filter(id=idx)


class FoodManusView(generics.ListCreateAPIView):
    queryset = FoodManus.objects.all()
    serializer_class = FoodManusSerializer
    pagination_class = DisplaySize
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_class = FoodManusFilter


class FoodManusRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FoodManusSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return FoodManus.objects.none()

        idx = self.kwargs['pk']
        # only the FoodManus owner or profile_manager (role) can change details
        return FoodManus.objects.filter(id=idx)


class VoteView(generics.CreateAPIView):
    serializer_class = VotesSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request, **kwargs):
        restaurant = request.data['restaurant']
        employee = request.data['employee']
        launch_end_time = 13 # 01:00PM
        if datetime.today().hour < launch_end_time:
            vote_with_exist_restaurant = Votes.objects.filter(restaurant=restaurant, day=datetime.today().date()).first()
            if vote_with_exist_restaurant:
                vote_with_exist_restaurant.employee.add(employee)
            else:
                create_vote_with_restaurant = Votes.objects.create(restaurant=restaurant, day=datetime.today().date())
                create_vote_with_restaurant.employee.add(employee)
            return Response({'details': 'Success' }, status=200)
        else:
            return Response({'details': 'Vote is not accepting now'}, status=400)

