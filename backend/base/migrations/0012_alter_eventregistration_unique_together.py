# Generated by Django 5.0 on 2024-01-06 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_eventregistration_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='eventregistration',
            unique_together=set(),
        ),
    ]
