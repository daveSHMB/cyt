# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0005_auto_20161122_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='strip',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='strip',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
