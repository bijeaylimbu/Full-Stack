# Generated by Django 3.1.5 on 2021-02-01 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_add', '0023_auto_20210201_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postadd_car',
            name='image',
            field=models.ImageField(default='mero', upload_to=''),
        ),
    ]