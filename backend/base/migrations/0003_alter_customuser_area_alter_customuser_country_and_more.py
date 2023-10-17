# Generated by Django 4.2.5 on 2023-10-09 16:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_customuser_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='area',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='country',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='house',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='landmark',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=255, null=True, validators=[django.core.validators.RegexValidator(message='phone number should exactly be in 10 digits', regex='^\\d{10}$')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='pincode',
            field=models.CharField(blank=True, default='', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='state',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='town',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]