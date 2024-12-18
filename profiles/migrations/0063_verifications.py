# Generated by Django 5.0.6 on 2024-11-08 23:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0062_rename_group_sex_interest_group_sex_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Verifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2048)),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verifyer', to=settings.AUTH_USER_MODEL)),
                ('verifyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verifyee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
