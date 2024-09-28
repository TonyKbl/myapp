# Generated by Django 5.0.6 on 2024-09-27 16:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0040_delete_myimage'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=10)),
                ('level_name', models.CharField(default='Free Memebr', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='level', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]