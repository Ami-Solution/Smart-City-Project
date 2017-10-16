# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-16 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_featurelocationmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessFeatureModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businessType', models.CharField(default='', max_length=100)),
                ('associatedCity', models.CharField(default='', max_length=100)),
                ('cityOrganisationalData', models.TextField()),
                ('stateAnalysis', models.TextField()),
                ('furtherReadings', models.TextField()),
                ('useMap', models.BooleanField()),
                ('optionalMapSearchInput', models.CharField(default='---', max_length=100)),
            ],
        ),
    ]
