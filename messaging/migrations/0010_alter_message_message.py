# Generated by Django 5.0.6 on 2024-09-18 11:09

import profanity.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0009_alter_message_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(blank=True, null=True, validators=[profanity.validators.validate_is_profane]),
        ),
    ]