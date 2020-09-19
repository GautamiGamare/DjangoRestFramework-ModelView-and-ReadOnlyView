from django.shortcuts import render
from app1.serializers import ProductSerializer,ProductModel
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet

class Product(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()

class ProductRead(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()
