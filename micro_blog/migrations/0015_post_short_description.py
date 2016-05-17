# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_blog', '0014_auto_20160422_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short_description',
            field=models.CharField(default='', help_text='This will be displayed in the site blog list pages.', max_length=250),
        ),
    ]
