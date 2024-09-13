# Generated by Django 5.0.6 on 2024-09-12 23:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0004_alter_message_attachment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msg_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg_from', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='msg_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg_to', to=settings.AUTH_USER_MODEL),
        ),
    ]