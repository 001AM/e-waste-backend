# Generated by Django 4.2.5 on 2024-01-19 17:40

import base.register.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_remove_education_content_education_content1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='email',
            field=base.register.models.LowercaseEmailField(max_length=254, null=True, unique=True, verbose_name='email address'),
        ),
    ]