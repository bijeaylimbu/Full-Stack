# Generated by Django 3.1.6 on 2021-02-17 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_add', '0049_auto_20210216_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postadd_landhouse',
            name='bathroom',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='postadd_landhouse',
            name='builtUp',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='postadd_landhouse',
            name='contact',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]