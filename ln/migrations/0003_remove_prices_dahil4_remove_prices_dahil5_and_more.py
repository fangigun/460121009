# Generated by Django 4.1.2 on 2023-01-03 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ln', '0002_alter_prices_dahil4_alter_prices_dahil5_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prices',
            name='dahil4',
        ),
        migrations.RemoveField(
            model_name='prices',
            name='dahil5',
        ),
        migrations.RemoveField(
            model_name='prices',
            name='dahil6',
        ),
        migrations.RemoveField(
            model_name='prices',
            name='dahil7',
        ),
    ]