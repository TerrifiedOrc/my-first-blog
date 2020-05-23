# Generated by Django 2.2.12 on 2020-05-21 12:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200521_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='education',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='education',
            name='foreignKey',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog.CV'),
        ),
        migrations.AddField(
            model_name='education',
            name='last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employment',
            name='foreignKey',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog.CV'),
        ),
    ]
