# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 03:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.OneToOneField(max_length=32, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('firstname', models.CharField(blank=True, max_length=64)),
                ('lastname', models.CharField(blank=True, max_length=64)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[(b'M', b'male'), (b'F', b'female'), (b'N', b'unknown')], max_length=1)),
                ('gitURL', models.CharField(blank=True, max_length=200)),
                ('approved', models.BooleanField(default=False)),
                ('friend', models.ManyToManyField(blank=True, related_name='_author_friend_+', to='author.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followee', to='author.Author')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='author.Author')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('follower', 'followee')]),
        ),
    ]
