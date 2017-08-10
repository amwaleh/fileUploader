# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 08:26
from __future__ import unicode_literals

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='download',
            field=models.URLField(default=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='uploads/', validators=[api.models.validate_file_extension]),
        ),
    ]