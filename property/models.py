import phonenumbers
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    owner = models.CharField('ФИО владельца', max_length=200)
    owner_pure_phone = PhoneNumberField('Номер владельца', region='RU', blank=True)
    new_building = models.BooleanField(verbose_name='Новостройка', default=False, null=True)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)

    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')

    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')

    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)

    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    liked = models.ManyToManyField(
        User,
        verbose_name='Кто лайкнул',
        related_name='liked_flat',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Owner(models.Model):
    name = models.CharField(max_length=50, verbose_name='ФИО влалельца')
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    normalized_owner_number = PhoneNumberField(
        region='RU',
        verbose_name='Нормализованный номер телефона',
        blank=True,
        null=True
    )
    apartments_owner = models.ManyToManyField(
        Flat,
        verbose_name='Квартиры в собственности',
        related_name='card_owner',
    )


class Complaint(models.Model):
    name_user = models.ForeignKey(User, verbose_name='Имя пользователя', on_delete=models.CASCADE)
    flat = models.ForeignKey(Flat, verbose_name='Жалоба на квартиру', on_delete=models.CASCADE)
    text_complaint = models.TextField(verbose_name='Сообщение', blank=True)

    def __str__(self):
        return self.flat.owner
