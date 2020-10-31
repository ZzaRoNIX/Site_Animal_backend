from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import generics
from xlrd import sheet

from .models import *
from .serializers import *

import openpyxl
from pathlib import Path


@api_view(['GET'])
def animals_detail(request, id):
    try:
        animal = Animal.objects.get(id=id)
    except Animal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AnimalSerializer(animal, context={'request': request})
        return Response(serializer.data)


# @api_view(['GET'])
# def animals_list(request):
#     """
#     List of animals.
#     """
#     if request.method == 'GET':
#         data = []
#         next_page = 1
#         previous_page = 1
#         animals = Animal.objects.all().order_by('-createdAt')
#         page = request.GET.get('page', 1)
#         paginator = Paginator(animals, 10)
#         try:
#             data = paginator.page(page)
#         except PageNotAnInteger:
#             data = paginator.page(1)
#         except EmptyPage:
#             data = paginator.page(paginator.num_pages)
#         serializer = AnimalListSerializer(data, context={'request': request}, many=True)
#         if data.has_next():
#             next_page = data.next_page_number()
#         if data.has_previous():
#             previous_page = data.previous_page_number()
#         return Response({'data': serializer.data,
#                          'count': paginator.count,
#                          'numpages': paginator.num_pages,
#                          'nextlink': '/api/animals/?page=' + str(next_page),
#                          'prevlink': '/api/animals/?page=' + str(previous_page)})
#
# # @api_view(['POST'])
# # def animals_list(request):
#
#
# @api_view(['GET'])
# def order_detail(request, id):
#     try:
#         order = Order.objects.get(id=id)
#     except Order.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = OrderSerializer(order, context={'request': request})
#         return Response(serializer.data)

@api_view(['GET'])
def excel_view(request):
    xlsx_file = Path('Data set.xlsx')
    wb_obj = openpyxl.load_workbook(xlsx_file)
    sheet = wb_obj.active

    firstCell = sheet['B3']
    lastCell = sheet['BC245']
    mas = []
    for j in range(firstCell.row, lastCell.row):
        mos = []
        for i in range(firstCell.column, lastCell.column):
            if i == 26 or i == 27 or i == 29 or i == 30 or i == 32 or i == 33 or i == 34 or i == 35 or i == 36:
                i = i
            else:
                c = sheet.cell(row=j, column=i).value
                mos.append(c)
        mas.append(mos)
    # user id=1 - admin
    for i in mas:
        # head_ofshelter_animal = '' - имя пользователя

        animal = Animal(author=User.objects.get(id=1), idcard_registration_animal=i[0],
                        type_animal=i[1], age_animal=i[2],
                        weight_animal=i[3], name_animal=i[4],
                        gender_animal=i[5], breed_animal=i[6], color_animal=i[7],
                        hair_animal=i[8], ears_animal=i[9], tail_animal=i[10],
                        size_animal=i[11], feature_animal=i[12], avairy_animal=i[13],
                        identification_mark_animal=i[14], sterilization_date_animal=i[15],
                        veterinarian_name_animal=i[16], socialized_animal=i[17],
                        receipt_report_animal=i[18], date_receipt_report_animal=i[19],
                        administrative_district_animal=i[20], catch_report_animal=i[21],
                        catching_address_animal=i[22], legal_entity_animal=i[23],
                        guardians_animal=i[24], natural_person_animal=i[25],
                        date_admission_toshelter_animal=i[26], act_animal=i[27],
                        date_leaving_shelter_animal=i[28], reason_leaving_animal=i[29],
                        contract_leaving_animal=i[30], shelter_address_animal=i[31],
                        exploit_organization_animal=i[32], head_ofshelter_animal=i[33],
                        care_worker_animal=i[34], item_no_treatment_animal=i[35],
                        date_treatment_parasite_animal=i[36], drug_name_animal=i[37],
                        drug_dosage_animal=i[38], item_no_vaccine_animal=i[39],
                        date_vaccine_animal=i[40], type_vaccine_animal=i[41],
                        num_serial_animal=i[42], date_inspection_animal=i[43])
        animal.save()
        print(animal)
    # print(mass)


@api_view(['GET'])
def animal_list(request):
    """
    List of animals.
    """
    if request.method == 'GET':
        data = []
        next_page = 1
        previous_page = 1
        animals = Animal.objects.all().order_by('idcard_registration_animal')
        page = request.GET.get('page', 1)
        paginator = Paginator(animals, 20)
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
