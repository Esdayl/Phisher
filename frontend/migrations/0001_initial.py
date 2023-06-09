# Generated by Django 3.2.16 on 2023-04-04 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('click_text', models.CharField(max_length=200)),
                ('click_date', models.DateTimeField(verbose_name='click date')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.email')),
            ],
        ),
    ]
