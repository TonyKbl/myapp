# Generated by Django 5.0.6 on 2024-09-27 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0041_level_userlevel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='level',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='level',
            name='level_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
