from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
#import requests, json

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import ListAPIView
from .serializers import ProductSerializer
from .paginations import ProductPagination
from .models import Products


# Create your views here.
class ProductCreation(APIView):
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AllProductView1(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    #pagination_class = ProductPagination
    
class AllProductView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    
class ProductViewALL(APIView):
    def get(self, request, format=None):
        snippets = Products.objects.all()
        serializer = ProductSerializer(snippets, many=True)
        return Response(serializer.data)

class ProductList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
