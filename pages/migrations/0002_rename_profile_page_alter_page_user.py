# Generated by Django 4.0 on 2024-06-29 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0026_alter_profile_dob2_alter_profile_height_and_more'),
        ('parties', '0002_rename_user_parties_page'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Page',
        ),
        migrations.AlterField(
            model_name='page',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='page', to='profiles.profile'),
        ),
    ]
