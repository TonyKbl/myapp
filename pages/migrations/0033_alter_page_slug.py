# Generated by Django 5.0.6 on 2024-07-01 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0032_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]