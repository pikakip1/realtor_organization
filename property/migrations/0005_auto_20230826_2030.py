from django.db import migrations


def checking_the_year_of_construction(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gte=2015).update(new_building=True)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20230826_2029'),
    ]

    operations = [
        migrations.RunPython(checking_the_year_of_construction)
    ]
