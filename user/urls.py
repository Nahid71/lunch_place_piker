
from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.CreateUserView.as_view(), name='user_signup'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.LogoutView.as_view(), name='user_logout'),
    path('userModify/<pk>/', views.UserRUDView.as_view(), name='user_update'),
]