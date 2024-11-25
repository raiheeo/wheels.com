from django.urls import path
from .views import CarViewSet


urlpatterns = [
    path('', CarViewSet.as_view({'get': 'list',
                                 'post': 'create'}), name='car_list'),

    path('<int:pk>/', CarViewSet.as_view({'get': 'retrieve',
                                          'put': 'update',
                                          'delete': 'destroy'}), name='car_detail')
]