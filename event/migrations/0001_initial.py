# Generated by Django 5.0.6 on 2024-10-21 08:33

import django.db.models.deletion
import django_resized.forms
import event.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0028_alter_page_cover_image_alter_page_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('ot_men', models.BooleanField(blank=True)),
                ('ot_women', models.BooleanField(blank=True)),
                ('ot_mfcouples', models.BooleanField(blank=True)),
                ('ot_ffcouples', models.BooleanField(blank=True)),
                ('ot_mmcoouples', models.BooleanField(blank=True)),
                ('ot_tvts', models.BooleanField(blank=True)),
                ('organiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organiser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('masterevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='event.masterevent')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=200, null=True, quality=-1, scale=None, size=[600, 600], upload_to=event.models.PathAndRename('event_images/2024/10/21'))),
                ('Location', models.CharField(max_length=255, null=True)),
            ],
            bases=('event.masterevent',),
        ),
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('masterevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='event.masterevent')),
                ('meet_type', models.CharField(choices=[('SOC', 'Social'), ('CLUB', 'Club Meet'), ('OURS', 'Meet at ours'), ('YOURS', 'Meet at yours')])),
                ('Location', models.CharField(max_length=255, null=True)),
            ],
            bases=('event.masterevent',),
        ),
        migrations.CreateModel(
            name='PrivateParty',
            fields=[
                ('masterevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='event.masterevent')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=200, null=True, quality=-1, scale=None, size=[600, 600], upload_to=event.models.PathAndRename('event_images/2024/10/21'))),
                ('Location', models.CharField(max_length=255, null=True)),
            ],
            bases=('event.masterevent',),
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('masterevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='event.masterevent')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=200, null=True, quality=-1, scale=None, size=[600, 600], upload_to=event.models.PathAndRename('event_images/2024/10/21'))),
                ('Location', models.CharField(max_length=255, null=True)),
            ],
            bases=('event.masterevent',),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('admission_fees', models.TextField(null=True)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('private', models.BooleanField(default=0)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='master_event', to='event.masterevent')),
            ],
        ),
        migrations.CreateModel(
            name='ClubEvent',
            fields=[
                ('masterevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='event.masterevent')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=200, null=True, quality=-1, scale=None, size=[600, 600], upload_to=event.models.PathAndRename('event_images/2024/10/21'))),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='pages.page')),
            ],
            bases=('event.masterevent',),
        ),
    ]
