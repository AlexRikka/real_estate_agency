# Generated by Django 2.2.24 on 2024-03-02 19:14

from django.db import migrations


def fill_field_new_building(apps, schema_editor):
    """Fills in new_building filed for all objects."""

    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gt=2015).update(new_building=True)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_field_new_building),
    ]
