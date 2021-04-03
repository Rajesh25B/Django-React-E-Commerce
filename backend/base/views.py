# django & DRF imports
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# local imports
from .models import Product
from .products import products
from .serializers import ProductSerializer
# Create your views here.

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
def getProducts(request): # returns all products from products.py
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk): # returns single product from all products
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)        
    return Response(serializer.data)
