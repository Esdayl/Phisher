# Generated by Django 3.2.16 on 2023-04-04 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20230404_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='compromised',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='link_opened',
            field=models.NullBooleanField(),
        ),
    ]