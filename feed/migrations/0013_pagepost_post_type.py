# Generated by Django 5.0.6 on 2024-07-19 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0012_alter_pagepost_name_alter_pagepost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagepost',
            name='post_type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]