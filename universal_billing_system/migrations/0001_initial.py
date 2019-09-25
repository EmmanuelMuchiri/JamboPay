# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-25 09:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Business_name', models.TextField(max_length=60)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_number', models.CharField(max_length=60)),
                ('Physical_address', models.TextField()),
                ('Post_code', models.CharField(max_length=20)),
                ('Town', models.TextField(max_length=30)),
                ('Industry', models.TextField(max_length=30)),
                ('JP_paybill', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universal_billing_system.Merchant')),
            ],
        ),
        migrations.AddField(
            model_name='industry',
            name='Merchant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universal_billing_system.Merchant'),
        ),
    ]