# Generated by Django 4.0 on 2024-06-15 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_profile_name_profile_name2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sexuality2',
            field=models.CharField(blank=True, choices=[('', 'Select Sexuality'), ('ST', 'Straight'), ('BI', 'Bisexial'), ('BC', 'Bi Curious'), ('BO', 'Orally Bi'), ('BP', 'Playfully Bi'), ('G', 'Gay'), ('L', 'Lesbian')], default='', max_length=2, null=True),
        ),
    ]
