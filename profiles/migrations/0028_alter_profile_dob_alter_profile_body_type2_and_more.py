# Generated by Django 5.0.6 on 2024-07-03 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0027_profile_body_type_profile_body_type2_profile_drink_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='DOB',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='body_type2',
            field=models.CharField(blank=True, choices=[('', 'Select Profile Type'), ('Slim', 'Slim'), ('Athletic', 'Athletic'), ('Curvy', 'Curvy'), ('Dad Bod', 'Dad Bod'), ('Large', 'Large')], default='', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='drink2',
            field=models.CharField(blank=True, choices=[('', 'Select Option'), ('Never', 'Never'), ('Occasionally', 'Occasionally'), ('Socially', 'Socially'), ('Often', 'Often'), ('Vape', 'Vape')], default='', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='smoke2',
            field=models.CharField(blank=True, choices=[('', 'Select Smoker Type'), ('Never', 'Never'), ('Occasionally', 'Occasionally'), ('Socially', 'Socially'), ('Often', 'Often'), ('Vape', 'Vape')], default='', max_length=16, null=True),
        ),
    ]
