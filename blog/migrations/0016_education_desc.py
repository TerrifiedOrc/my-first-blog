# Generated by Django 2.2.12 on 2020-05-23 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200522_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='desc',
            field=models.TextField(default='', max_length=200),
        ),
    ]