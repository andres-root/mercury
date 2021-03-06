# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-09 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('origin', models.CharField(blank=True, max_length=255, null=True)),
                ('destination', models.CharField(blank=True, max_length=255, null=True)),
                ('cost', models.CharField(blank=True, max_length=255, null=True)),
                ('departure_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('discount', models.CharField(blank=True, max_length=255, null=True)),
                ('segment', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
