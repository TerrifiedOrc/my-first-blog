# Generated by Django 2.2.12 on 2020-05-20 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_cv_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='phone',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='cv',
            name='address',
            field=models.TextField(default='', max_length=200),
        ),
    ]
