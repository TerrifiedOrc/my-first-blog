# Generated by Django 2.2.12 on 2020-05-22 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200521_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='education',
            name='last_updated',
        ),
        migrations.AlterField(
            model_name='education',
            name='endDate',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='startDate',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employment',
            name='endDate',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employment',
            name='startDate',
            field=models.TextField(blank=True, null=True),
        ),
    ]
