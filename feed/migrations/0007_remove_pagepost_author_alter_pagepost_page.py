# Generated by Django 5.0.6 on 2024-07-18 02:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_pagepost'),
        ('pages', '0003_alter_page_cover_image_alter_page_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagepost',
            name='author',
        ),
        migrations.AlterField(
            model_name='pagepost',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages_posts', to='pages.page'),
        ),
    ]
