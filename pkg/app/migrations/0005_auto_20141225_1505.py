# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20141225_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='file_size',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
