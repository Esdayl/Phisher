# Generated by Django 3.2.16 on 2023-04-04 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('link_opened', models.IntegerField()),
                ('compromised', models.IntegerField()),
                ('token', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Click',
        ),
        migrations.DeleteModel(
            name='Email',
        ),
    ]
