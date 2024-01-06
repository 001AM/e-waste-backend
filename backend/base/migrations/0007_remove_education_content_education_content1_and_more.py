# Generated by Django 4.2.5 on 2024-01-04 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_education_created_on_alter_education_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='content',
        ),
        migrations.AddField(
            model_name='education',
            name='content1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='content2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='content3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='backend'),
        ),
    ]