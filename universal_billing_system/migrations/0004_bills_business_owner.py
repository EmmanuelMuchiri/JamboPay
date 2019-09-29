# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-29 08:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('universal_billing_system', '0003_auto_20190929_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='business_owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
