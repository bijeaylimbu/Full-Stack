# Generated by Django 3.1.5 on 2021-02-01 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_add', '0022_auto_20210201_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postadd_car',
            old_name='username_id',
            new_name='username',
        ),
    ]
