from django.shortcuts import render
from rest_framework import viewsets
from .models import Agency, Zone, Category
from .serializers import AgencySerializer, ZoneSerializer, CategorySerializer
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the G_agence index.")


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AgencyViewSet(viewsets.ModelViewSet):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer

