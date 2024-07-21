# Generated by Django 5.0.6 on 2024-07-18 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0033_alter_profile_description_alter_profile_headline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='body_type',
            field=models.CharField(choices=[('', 'Select Body Type'), ('Slim', 'Slim'), ('Athletic', 'Athletic'), ('Curvy', 'Curvy'), ('Dad Bod', 'Dad Bod'), ('Large', 'Large')], default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='profile',
            name='body_type2',
            field=models.CharField(blank=True, choices=[('', 'Select Body Type'), ('Slim', 'Slim'), ('Athletic', 'Athletic'), ('Curvy', 'Curvy'), ('Dad Bod', 'Dad Bod'), ('Large', 'Large')], default='', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='drink',
            field=models.CharField(choices=[('', 'Select Option'), ('Never', 'Never'), ('Occasionally', 'Occasionally'), ('Socially', 'Socially'), ('Often', 'Often')], default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='profile',
            name='drink2',
            field=models.CharField(blank=True, choices=[('', 'Select Option'), ('Never', 'Never'), ('Occasionally', 'Occasionally'), ('Socially', 'Socially'), ('Often', 'Often')], default='', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.CharField(choices=[('', 'Select Height'), ('4ft 11in', '<5ft'), ('5ft 0in', '5ft 0in'), ('5ft 1in', '5ft 1in'), ('5ft 2in', '5ft 2in'), ('5ft 3in', '5ft 3in'), ('5ft 4in', '5ft 4in'), ('5ft 5in', '5ft 5in'), ('5ft 6in', '5ft 6in'), ('5ft 7in', '5ft 7in'), ('5ft 8in', '5ft 8in'), ('5ft 9in', '5ft 9in'), ('5ft 10in', '5ft 10in'), ('5ft 11in', '5ft 11in'), ('6ft 0in', '6ft 0in'), ('6ft 1in', '6ft 1in'), ('6ft 2in', '6ft 2in'), ('6ft 3in', '6ft 3in'), ('6ft 4in', '6ft 4in'), ('6ft 5in', '6ft 5in'), ('6ft 6in', '6ft 6in'), ('6ft 7in', '>6ft 6in')], default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height2',
            field=models.CharField(blank=True, choices=[('', 'Select Height'), ('4ft 11in', '<5ft'), ('5ft 0in', '5ft 0in'), ('5ft 1in', '5ft 1in'), ('5ft 2in', '5ft 2in'), ('5ft 3in', '5ft 3in'), ('5ft 4in', '5ft 4in'), ('5ft 5in', '5ft 5in'), ('5ft 6in', '5ft 6in'), ('5ft 7in', '5ft 7in'), ('5ft 8in', '5ft 8in'), ('5ft 9in', '5ft 9in'), ('5ft 10in', '5ft 10in'), ('5ft 11in', '5ft 11in'), ('6ft 0in', '6ft 0in'), ('6ft 1in', '6ft 1in'), ('6ft 2in', '6ft 2in'), ('6ft 3in', '6ft 3in'), ('6ft 4in', '6ft 4in'), ('6ft 5in', '6ft 5in'), ('6ft 6in', '6ft 6in'), ('6ft 7in', '>6ft 6in')], default='', max_length=16, null=True),
        ),
    ]