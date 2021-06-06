from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from .serializers import CustomUserSerializer, UserLoginSerializer, UserLogoutSerializer
from .models import CustomUser
# Create your views here.

class CreateUserView(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = []
    authentication_classes = []
    # pagination_class = DisplaySize

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data,  context={"request": request})
        if serializer.is_valid():
            inst = serializer.save()
            inst.is_active = True
            inst.is_staff = True
            xpassword = inst.password
            inst.set_password(xpassword)
            inst.save()
            res_data = serializer.data
           

            return Response(res_data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def get_queryset(self):
        return CustomUser.objects.all().exclude(email='admin@innotool.com')


class UserRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        inst = self.get_object()
        if 'first_name' in request.data:
            inst.first_name = request.data['first_name']
            
        if 'last_name' in request.data:
            inst.last_name = request.data['last_name']
            
        if 'email' in request.data:
            inst.email = request.data['email']

        if 'password' in request.data:
            inst.set_password(request.data['password'])

        if 'profile_pic' in request.data:
            inst.profile_pic = request.data['profile_pic']
        
        inst.save()
        
        serializer = self.get_serializer(inst, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    


class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request, **kwargs):
        email = request.data['email']
        password = request.data['password']
        print(email, password)
        if email == 'admin@rp.com':
            return Response({'details': 'Invalid Credentials', 'meta': f"Restrcted access! for {email}"}, status=400)
        user = authenticate(email=email, password=password)
        if user:
            serializer = CustomUserSerializer(user, many=False, context={"request": request})
            token, _created = Token.objects.get_or_create(user=user)
            dikt = {}
            dikt.update(serializer.data)
            dikt.update({'token': token.key})
            return Response(dikt, status=200)
        else:
            return Response({'details': 'Invalid Credentials'}, status=400)


class LogoutView(generics.CreateAPIView):
    serializer_class = UserLogoutSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, **kwargs):
        request.user.auth_token.delete() #deleting the token for this user
        return Response({'details': 'Success' }, status=200)