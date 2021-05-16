# django & DRF imports
from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

# local imports
from base.models import Product
from base.products import products
from base.serializers import ProductSerializer

# Create your views here.

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

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = Product.objects.get(_id=pk)
    product.delete()
    return Response('Product was deleted')
