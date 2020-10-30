from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import generics
from .models import *
from .serializers import *


@api_view(['GET'])
def animals_detail(request, id):
    try:
        animal = Animal.objects.get(id=id)
    except Animal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AnimalSerializer(animal, context={'request': request})
        return Response(serializer.data)


@api_view(['GET'])
def animals_list(request):
    """
    List of animals.
    """
    if request.method == 'GET':
        data = []
        next_page = 1
        previous_page = 1
        animals = Animal.objects.all().order_by('-createdAt')
        page = request.GET.get('page', 1)
        paginator = Paginator(animals, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        serializer = AnimalListSerializer(data, context={'request': request}, many=True)
        if data.has_next():
            next_page = data.next_page_number()
        if data.has_previous():
            previous_page = data.previous_page_number()
        return Response({'data': serializer.data,
                         'count': paginator.count,
                         'numpages': paginator.num_pages,
                         'nextlink': '/api/animals/?page=' + str(next_page),
                         'prevlink': '/api/animals/?page=' + str(previous_page)})

# @api_view(['POST'])
# def animals_list(request):


@api_view(['GET'])
def order_detail(request, id):
    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order, context={'request': request})
        return Response(serializer.data)
