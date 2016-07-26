# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 17:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_authorexample_blogexample_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='user',
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]