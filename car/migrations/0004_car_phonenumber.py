# Generated by Django 3.1.7 on 2021-09-16 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_remove_car_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='phonenumber',
            field=models.CharField(max_length=15, null=True),
        ),
    ]