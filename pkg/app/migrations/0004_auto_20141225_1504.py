# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20141225_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
