# Generated by Django 3.1.5 on 2021-02-05 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_add', '0034_postadd_car_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postadd_car',
            name='date',
        ),
    ]