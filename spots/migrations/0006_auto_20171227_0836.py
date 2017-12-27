# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-27 08:36
from __future__ import unicode_literals

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0005_auto_20171226_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='geom',
            field=djgeojson.fields.PointField(default=dict),
        ),
        migrations.AlterField(
            model_name='event',
            name='datum',
            field=models.DateField(blank=True, null=True),
        ),
    ]
