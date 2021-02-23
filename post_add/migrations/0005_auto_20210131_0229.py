# Generated by Django 3.1.5 on 2021-01-31 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_add', '0004_auto_20210128_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postadd_car',
            name='color',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='postadd_car',
            name='delivery_area',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='postadd_car',
            name='engine',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='postadd_car',
            name='home_delivery',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=6),
        ),
        migrations.AlterField(
            model_name='postadd_car',
            name='kilometers',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='postadd_car',
            name='lot',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='postadd_car',
            name='milage',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='postadd_car',
            name='price',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='postadd_car',
            name='warrenty',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=6),
        ),
        migrations.AlterField(
            model_name='postadd_car',
            name='warrenty_period',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]