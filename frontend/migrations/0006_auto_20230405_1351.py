# Generated by Django 3.2.16 on 2023-04-05 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_alter_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='compromised',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='link_opened',
            field=models.BooleanField(default=False),
        ),
    ]
