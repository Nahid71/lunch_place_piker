from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from .serializers import CustomUserSerializer
from .models import CustomUser
# Create your views here.

class CreateUserView(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = []
    authentication_classes = []
    # pagination_class = DisplaySize

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data,  context={"request": request})
        if serializer.is_valid():
            inst = serializer.save()
            inst.is_active = True
            inst.is_staff = True
            xpassword = inst.password
            inst.set_password(xpassword)
            inst.save()
            res_data = serializer.data
           

            return Response(res_data, status=200)
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

