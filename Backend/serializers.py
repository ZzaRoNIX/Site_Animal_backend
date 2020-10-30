from rest_framework import serializers
from .models import *
from rest_framework import fields


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('id', 'author', 'moniker_animal', 'weight_animal',
                  'height_animal', 'gender_animal', 'born_on_animal',
                  'type_color_animal', 'color_animal', 'hair_animal',
                  'sterilization_animal', 'trained_animal', 'vaccinations_animal',
                  'adress_animal', 'status_animal')


class AnimalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('id', 'author', 'moniker_animal', 'createdAt', 'gender_animal')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'animal_id', 'first_name_order', 'second_name_order', 'patronymic_name_order')
