# Generated by Django 5.0.6 on 2024-09-15 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0006_alter_message_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date_read',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='date_sent',
            field=models.DateField(auto_now=True),
        ),
    ]