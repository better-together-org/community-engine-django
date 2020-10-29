# Generated by Django 3.0.5 on 2020-05-01 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('better_together', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='person',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]