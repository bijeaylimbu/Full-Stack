# Generated by Django 3.1.5 on 2021-02-11 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_add', '0041_auto_20210211_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postadd_computer',
            name='usedFor',
            field=models.DateField(blank=True),
        ),
    ]
