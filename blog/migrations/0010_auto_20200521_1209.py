# Generated by Django 2.2.12 on 2020-05-21 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200521_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
