# django & DRF imports
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.hashers import make_password
from rest_framework import status

# local imports
from base.models import Product
from django.contrib.auth.models import User
from base.serializers import ProductSerializer, UserSerializer, UserSerializerWithToken

# simpleJWT imports
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    '''Serializer to obtain the username and email from the token'''
    
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        serializer = UserSerializerWithToken(self.user).data

        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def registerUser(request):

    data = request.data

    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )
        
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)

    except:
        message = {'detail': 'User with this email already exist'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request): # returns the user
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request): # returns all users only for admin user
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
