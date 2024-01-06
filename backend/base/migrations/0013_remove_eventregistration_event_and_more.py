# Generated by Django 5.0 on 2024-01-06 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_eventregistration_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventregistration',
            name='event',
        ),
        migrations.RemoveField(
            model_name='eventregistration',
            name='registration_date',
        ),
        migrations.RemoveField(
            model_name='eventregistration',
            name='user',
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='event_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]