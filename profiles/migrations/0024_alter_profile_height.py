# Generated by Django 4.0 on 2024-06-28 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0023_profile_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.CharField(choices=[('', 'Select Sexuality'), ('meN', 'ME CHOICES'), ('Bisexual', 'Bisexual'), ('Bicurious', 'Bicuriuos'), ('Orally Bi', 'Orally Bi'), ('Bi Playful', 'Bi Playful'), ('Gay', 'Gay'), ('Lesbian', 'Lesbian')], default='', max_length=16),
        ),
    ]