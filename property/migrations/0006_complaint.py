# Generated by Django 2.2.24 on 2023-08-27 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0005_auto_20230826_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Flat')),
                ('name_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]