from rest_framework import serializers
from .models import Marka, Model, Car


class MarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'title', 'description', 'color', 'price', 'volume', 'type_change', 'image', 'video', 'year', 'created_date', 'marka', 'model' ]

