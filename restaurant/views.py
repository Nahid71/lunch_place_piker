from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from datetime import datetime, timedelta
from .models import Restaurant, FoodItem, FoodManus, Votes, Winner
from restaurant_picker.pagination import DisplaySize
from .serializers import RestaurantSerializer, FoodItemSerializer, FoodManusSerializer, VotesSerializer, WinnerSerializer
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
        vote_start_time = 11 # 11:00AM
        vote_end_time = 13 # 01:00PM
        if datetime.today().hour < vote_end_time and datetime.today().hour > vote_start_time: # not accepting any vote
            vote_with_exist_restaurant = Votes.objects.filter(restaurant=restaurant, day=datetime.today().date()).first()
            if not vote_with_exist_restaurant:
                vote_with_exist_restaurant = Votes.objects.create(restaurant=restaurant, day=datetime.today().date())
            vote_with_exist_restaurant.employee.add(employee)
            vote_with_exist_restaurant.vote_count += 1
            vote_with_exist_restaurant.save()
            return Response({'details': 'Success' }, status=200)
        else:
            return Response({'details': 'Vote is not accepting now'}, status=400)

class Winner(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, **kwargs):
        vote_end_time = 13 # 01:00PM
        x = None
        if datetime.today().hour > vote_end_time:
            winner = Winner.objects.filter(day=datetime.today().date()).first()
            if winner:
                x = WinnerSerializer(winner, many=False).data
            else:
                last_1_day_winner = Winner.objects.filter(day=datetime.today().date() - timedelta(days=1)).first()
                last_2_day_winner = Winner.objects.filter(day=datetime.today().date()- timedelta(days=2)).first()
                last_3_day_winner = Winner.objects.filter(day=datetime.today().date()- timedelta(days=3)).first()
                winner = Votes.objects.filter(day=datetime.today().date()).order_by('vote_count')
                for each in winner:
                    if each.restaurant is not last_1_day_winner and each.restaurant is not last_2_day_winner and each.restaurant is not last_3_day_winner: # checking that the winner restaurant doesn't win for last 3 days
                        x = winner.objects.create(restaurant=each.restaurant, day=datetime.today().date())
                        x = WinnerSerializer(x, many=False).data
            return Response({'details': 'Success', 'data': x}, status=200)
        else:
            return Response({'details': 'Winner is not decided yet'}, status=400)
                    


