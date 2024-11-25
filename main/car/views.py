from .serializers import *
from .models import *
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CarFilter
from rest_framework.filters import SearchFilter, OrderingFilter



class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = CarFilter
    search_fields = ['title']
    ordering_fields = ['title', 'price', 'created_date']
    permission_classes = [permissions.IsAuthenticated]

class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class MarkaViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = MarkaSerializer





