# django & DRF imports
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# local imports
from .products import products
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
    return Response(products)

@api_view(['GET'])
def getProduct(request, pk): # returns single product from all products
    
    product = None
    
    for i in products:
        if i['_id'] == pk:
            product = i
            break
    
    return Response(product)
