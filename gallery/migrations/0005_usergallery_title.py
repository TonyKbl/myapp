# Generated by Django 5.0.6 on 2024-10-29 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_alter_usergallery_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergallery',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]