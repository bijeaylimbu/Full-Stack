# Generated by Django 3.1.6 on 2021-02-18 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0007_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default=True, max_length=255),
        ),
    ]