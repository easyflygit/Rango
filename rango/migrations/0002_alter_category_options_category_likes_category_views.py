# Generated by Django 4.0.2 on 2023-05-22 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0, max_length=6),
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
