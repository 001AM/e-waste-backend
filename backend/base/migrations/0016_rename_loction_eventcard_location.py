# Generated by Django 5.0 on 2024-01-07 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_eventregistration_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventcard',
            old_name='loction',
            new_name='location',
        ),
    ]
