from rest_framework import serializers
from .models import *
from rest_framework import fields


# class AnimalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Animal
#         fields = ('id', 'author', 'moniker_animal', 'weight_animal',
#                   'height_animal', 'gender_animal', 'born_on_animal',
#                   'type_color_animal', 'color_animal', 'hair_animal',
#                   'sterilization_animal', 'trained_animal', 'vaccinations_animal',
#                   'adress_animal', 'status_animal')

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('id', 'author', 'idcard_registration_animal',
                  'type_animal', 'age_animal', 'weight_animal', 'name_animal',
                  'gender_animal', 'breed_animal', 'color_animal',
                  'hair_animal', 'ears_animal', 'tail_animal',
                  'size_animal', 'feature_animal', 'avairy_animal',
                  'identification_mark_animal', 'sterilization_date_animal',
                  'veterinarian_name_animal', 'socialized_animal',
                  'receipt_report_animal', 'date_receipt_report_animal',
                  'administrative_district_animal', 'catch_report_animal',
                  'catching_address_animal', 'legal_entity_animal',
                  'guardians_animal', 'natural_person_animal',
                  'date_admission_toshelter_animal', 'act_animal',
                  'date_leaving_shelter_animal', 'reason_leaving_animal',
                  'contract_leaving_animal', 'shelter_address_animal',
                  'exploit_organization_animal', 'head_ofshelter_animal',
                  'care_worker_animal', 'item_no_treatment_animal',
                  'date_treatment_parasite_animal', 'drug_name_animal',
                  'drug_dosage_animal', 'item_no_vaccine_animal',
                  'date_vaccine_animal', 'type_vaccine_animal',
                  'num_serial_animal', 'date_inspection_animal',
                  'anamnesis_animal')


class AnimalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('id', 'author', 'idcard_registration_animal', 'name_animal', 'shelter_address_animal')


# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ('id', 'animal_id', 'first_name_order', 'second_name_order', 'patronymic_name_order')
