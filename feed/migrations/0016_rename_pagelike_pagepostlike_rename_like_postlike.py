# Generated by Django 5.0.6 on 2024-07-26 07:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0015_like_post_likes_pagelike_pagepost_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PageLike',
            new_name='PagePostLike',
        ),
        migrations.RenameModel(
            old_name='Like',
            new_name='PostLike',
        ),
    ]