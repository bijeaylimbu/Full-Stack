# Generated by Django 3.1.6 on 2021-02-21 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0039_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=255),
        ),
    ]