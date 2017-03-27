# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 02:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('trusted', models.BooleanField()),
                ('user', models.OneToOneField(max_length=32, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
