from django.db import models
from datetime import date
from multiselectfield import MultiSelectField
from rest_framework import fields
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# from rest_framework.fields import MultipleChoiceField


class Animal(models.Model):
    # img = models.ImageField('Аватар', null=True, upload_to=)

    TYPE_GENDER = (
        ('boy', 'Мальчик'),
        ('girl', 'Девочка'),
    )

    TYPE_COLOR = (
        ('monochrome', 'Монотонная'),
        ('multicolor', 'Многоцветная'),
    )

    CHOICES_COLORS = (
        ('black', 'Черная'),
        ('white', 'Белая'),
        ('brown', 'Коричневая'),
        ('grey', 'Серая'),
        ('redhead', 'Рыжая'),
        ('striped', 'Полосатая'),
        ('spotted', 'Пятнистая'),
    )

    TYPE_HAIR = (
        ('longhaired', 'Пушистая'),
        ('shorthaired', 'Короткошерстая'),
        ('hairless', 'Безволосая'),
    )

    TYPE_STERILIZATION = (
        ('yes', 'Да'),
        ('no', 'Нет'),
    )

    TYPE_TRAINED = (
        ('yes', 'Да'),
        ('no', 'Нет'),
    )
    CHOICES_STATUS = (
        ('avaible', 'Готов к социализации'),
        ('unavaible', 'Не готов к социализации'),
    )
    # user = models.ForeignKey(User, verbose_name='Пользователь', blank=True, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), verbose_name='Создатель', null=True, on_delete=models.CASCADE)
    moniker_animal = models.CharField('Кличка', max_length=100)
    createdAt = models.DateField('Дата создания', auto_now_add=True)
    weight_animal = models.IntegerField('Вес')
    height_animal = models.IntegerField('Рост', default='')
    gender_animal = models.CharField('Пол', choices=TYPE_GENDER, max_length=7)
    born_on_animal = models.DateField(verbose_name='Дата рождения', default=date.today)
    type_color_animal = models.CharField('Тип окраса', choices=TYPE_COLOR, max_length=10)
    color_animal = MultiSelectField(verbose_name='Цвет', choices=CHOICES_COLORS, max_length=1000)
    hair_animal = models.CharField('Шерсть', choices=TYPE_HAIR, max_length=100)
    sterilization_animal = models.CharField('Стерилизован', choices=TYPE_STERILIZATION, max_length=100)
    trained_animal = models.CharField('Дрессирован\приучен к лотку', choices=TYPE_TRAINED, max_length=100)
    vaccinations_animal = models.CharField('Прививки', max_length=255, default='Не привит')
    adress_animal = models.CharField('Адрес приюта', max_length=255)
    # (важный пункт - не готовых, не отправлять на фронт, заявку на них соответственно оставить будет нельзя)
    status_animal = models.CharField('Готовность к социализации', choices=CHOICES_STATUS, max_length=100, default='')

    def __str__(self):
        return self.moniker_animal

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animals'


class Order(models.Model):
    animal_id = models.IntegerField('ID животного')

    createdAt = models.DateField('Дата создания', auto_now_add=True)
    first_name_order = models.CharField('Имя', max_length=100)
    second_name_order = models.CharField('Фамилия', max_length=100)
    patronymic_name_order = models.CharField('Отчество', max_length=100)

    def __str__(self):
        return self.second_name_order
