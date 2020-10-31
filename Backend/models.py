from django.db import models
from datetime import date
from multiselectfield import MultiSelectField
from rest_framework import fields
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# from rest_framework.fields import MultipleChoiceField


# class Animal(models.Model):
#     # img = models.ImageField('Аватар', null=True, upload_to=)
#
#     TYPE_GENDER = (
#         ('boy', 'Мальчик'),
#         ('girl', 'Девочка'),
#     )
#
#     TYPE_COLOR = (
#         ('monochrome', 'Монотонная'),
#         ('multicolor', 'Многоцветная'),
#     )
#
#     CHOICES_COLORS = (
#         ('black', 'Черная'),
#         ('white', 'Белая'),
#         ('brown', 'Коричневая'),
#         ('grey', 'Серая'),
#         ('redhead', 'Рыжая'),
#         ('striped', 'Полосатая'),
#         ('spotted', 'Пятнистая'),
#     )
#
#     TYPE_HAIR = (
#         ('longhaired', 'Пушистая'),
#         ('shorthaired', 'Короткошерстая'),
#         ('hairless', 'Безволосая'),
#     )
#
#     TYPE_STERILIZATION = (
#         ('yes', 'Да'),
#         ('no', 'Нет'),
#     )
#
#     TYPE_TRAINED = (
#         ('yes', 'Да'),
#         ('no', 'Нет'),
#     )
#     CHOICES_STATUS = (
#         ('avaible', 'Готов к социализации'),
#         ('unavaible', 'Не готов к социализации'),
#     )
#     # user = models.ForeignKey(User, verbose_name='Пользователь', blank=True, null=True, on_delete=models.CASCADE)
#     author = models.ForeignKey(get_user_model(), verbose_name='Создатель', null=True, on_delete=models.CASCADE)
#     moniker_animal = models.CharField('Кличка', max_length=100)
#     createdAt = models.DateField('Дата создания', auto_now_add=True)
#     weight_animal = models.IntegerField('Вес')
#     height_animal = models.IntegerField('Рост', default='')
#     gender_animal = models.CharField('Пол', choices=TYPE_GENDER, max_length=7)
#     born_on_animal = models.DateField(verbose_name='Дата рождения', default=date.today)
#     type_color_animal = models.CharField('Тип окраса', choices=TYPE_COLOR, max_length=10)
#     color_animal = MultiSelectField(verbose_name='Цвет', choices=CHOICES_COLORS, max_length=1000)
#     hair_animal = models.CharField('Шерсть', choices=TYPE_HAIR, max_length=100)
#     sterilization_animal = models.CharField('Стерилизован', choices=TYPE_STERILIZATION, max_length=100)
#     trained_animal = models.CharField('Дрессирован\приучен к лотку', choices=TYPE_TRAINED, max_length=100)
#     vaccinations_animal = models.CharField('Прививки', max_length=255, default='Не привит')
#     adress_animal = models.CharField('Адрес приюта', max_length=255)
#     # (важный пункт - не готовых, не отправлять на фронт, заявку на них соответственно оставить будет нельзя)
#     status_animal = models.CharField('Готовность к социализации', choices=CHOICES_STATUS, max_length=100, default='')
class Animal(models.Model):
    # общие  сведения
    author = models.ForeignKey(get_user_model(), verbose_name='Создатель', null=True, on_delete=models.CASCADE)

    idcard_registration_animal = models.CharField('карточка учета животного №', max_length=100, default="", null=True)
    type_animal = models.CharField('вид', max_length=100, default='', null=True)
    age_animal = models.CharField('возраст', max_length=100, default='', null=True)
    weight_animal = models.CharField('вес', max_length=100, default='', null=True)
    name_animal = models.CharField('кличка', max_length=100, default='', null=True)
    gender_animal = models.CharField('пол', max_length=100, default='', null=True)
    breed_animal = models.CharField('порода', max_length=100, default='', null=True)
    color_animal = models.CharField('окрас', max_length=100, default='', null=True)
    hair_animal = models.CharField('шерсть', max_length=100, default='', null=True)
    ears_animal = models.CharField('уши', max_length=100, default='', null=True)
    tail_animal = models.CharField('хвост', max_length=100, default='', null=True)
    size_animal = models.CharField('размер', max_length=100, default='', null=True)
    feature_animal = models.CharField('особые приметы', max_length=100, default='', null=True)
    avairy_animal = models.CharField('Вольер №', max_length=100, default='', null=True)
    # дополнительные сведения
    identification_mark_animal = models.CharField('идентификационная метка', max_length=100, default='', null=True)
    sterilization_date_animal = models.CharField('дата стерилизации', max_length=100, default='', null=True)
    veterinarian_name_animal = models.CharField('ф.и.о. ветеринарного врача', max_length=200, default='', null=True)
    socialized_animal = models.CharField('Социализировано(да/нет)', max_length=100, default='', null=True)
    # сведения об отлове
    receipt_report_animal = models.CharField('заказ-наряд / акт о поступлении животного №', max_length=100, default='', null=True)
    date_receipt_report_animal = models.CharField('заказ-наряд дата/ акт о поступлении животного, дата', max_length=100, default='', null=True)
    administrative_district_animal = models.CharField('административный округ', max_length=100, default='', null=True)
    catch_report_animal = models.CharField('акт отлова №', max_length=100, default='', null=True)
    catching_address_animal = models.CharField('адрес места отлова', max_length=250, default='', null=True)
    # сведения о новых владельцах
    legal_entity_animal = models.CharField('юридическое лицо', max_length=100, default='FFF', null=True)
    guardians_animal = models.CharField('ф.и.о. опекунов', max_length=200, default='', null=True)
    natural_person_animal = models.CharField('физическое лицо ф.и.о.', max_length=200, default='', null=True)
    # движение животного
    date_admission_toshelter_animal = models.CharField('дата поступления в приют', max_length=20, default='', null=True)
    act_animal = models.CharField('акт №', max_length=100, default='', null=True)
    date_leaving_shelter_animal = models.CharField('дата выбытия из приюта', max_length=100, default='', null=True)
    reason_leaving_animal = models.CharField('причина выбытия', max_length=200, default='', null=True)
    contract_leaving_animal = models.CharField('акт/договор №', max_length=100, default='', null=True)
    # ответственные за животное
    shelter_address_animal = models.CharField('адрес приюта', max_length=300, default='', null=True)
    exploit_organization_animal = models.CharField('эксплуатирующая организация', max_length=100, default='', null=True)
    head_ofshelter_animal = models.CharField('ф.и.о. руководителя приюта', max_length=100, default='', null=True)
    care_worker_animal = models.CharField('ф.и.о. сотрудника по уходу за животным', max_length=100, default='', null=True)
    # сведения об обработке от экто- и эндопаразитов
    item_no_treatment_animal = models.CharField('№ п/п(сведения об обработке от экто- и эндопаразитов)', max_length=200, default='', null=True)
    date_treatment_parasite_animal = models.CharField('дата', max_length=100, default='', null=True)
    drug_name_animal = models.CharField('название препарата', max_length=1000, default='', null=True)
    drug_dosage_animal = models.CharField('доза', max_length=100, default='', null=True)
    # сведения о вакцинации
    item_no_vaccine_animal = models.CharField('№ п/п(сведения о вакцинации )', max_length=20, default='', null=True)
    date_vaccine_animal = models.CharField('дата', max_length=100, default='', null=True)
    type_vaccine_animal = models.CharField('вид вакцины', max_length=100, default='', null=True)
    num_serial_animal = models.CharField('№ серии', max_length=100, default='', null=True)
    # сведения о состоянии здоровья
    date_inspection_animal = models.CharField('дата осмотра', max_length=100, default='', null=True)
    anamnesis_animal = models.CharField('анамнез', max_length=100, default='', null=True)

    def __str__(self):
        return str(self.idcard_registration_animal)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animals'

# class Order(models.Model):
#     animal_id = models.IntegerField('ID животного')
#
#     createdAt = models.DateField('Дата создания', auto_now_add=True)
#     first_name_order = models.CharField('Имя', max_length=100)
#     second_name_order = models.CharField('Фамилия', max_length=100)
#     patronymic_name_order = models.CharField('Отчество', max_length=100)
#
#     def __str__(self):
#         return self.second_name_order
