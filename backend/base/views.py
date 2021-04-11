# django & DRF imports
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# local imports
from .models import Product
from django.contrib.auth.models import User
from .products import products
from .serializers import ProductSerializer, UserSerializer, UserSerializerWithToken
# Create your views here.

# simpleJWT imports
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

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

@api_view(['GET'])
def getRoutes(request):
    '''this view tells us what routes we have 
    and how our API is going to look at '''

    routes = [
        '/api/products/',
        '/api/products/create/',
        
        '/api/products/upload/',
        
        '/api/products/<id>/reviews/',
        
        '/api/products/top/',
        '/api/products/<id>/',

        '/api/products/delete<id>/',
        '/api/products/<update>/<id>/'
    ]
    return Response(routes)

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

@api_view(['GET'])
def getProducts(request): # returns all products from Product model
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk): # returns single product from all products
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)        
    return Response(serializer.data)
