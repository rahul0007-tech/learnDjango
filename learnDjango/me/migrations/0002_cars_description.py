# Generated by Django 5.0.8 on 2024-08-12 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
