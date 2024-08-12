# Generated by Django 5.0.8 on 2024-08-12 04:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('carImg', models.ImageField(upload_to='cars/')),
                ('registeredDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('carType', models.CharField(choices=[('SUV', 'SUV'), ('sedan', 'sedan')], max_length=15)),
            ],
        ),
    ]
