# Generated by Django 4.2.5 on 2024-01-06 14:41

import base.register.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_eventcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=100)),
                ('email', base.register.models.LowercaseEmailField(max_length=254, null=True, unique=True, verbose_name='email address')),
                ('phone', models.CharField(blank=True, default='', max_length=255, null=True, validators=[django.core.validators.RegexValidator(message='Phone number should exactly be in 10 digits', regex='^\\d{10}$')])),
                ('event_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='eventcard',
            old_name='loction',
            new_name='location',
        ),
        migrations.AlterField(
            model_name='eventcard',
            name='about',
            field=models.CharField(max_length=10000),
        ),
    ]
