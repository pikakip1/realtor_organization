# Generated by Django 2.2.28 on 2023-08-28 16:34

from django.conf import settings
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20230827_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='liked',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_flat', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('normalized_owner_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RU')),
                ('apartments_owner', models.ManyToManyField(related_name='card_owner', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
