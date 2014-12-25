# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20141225_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='group',
            field=models.ForeignKey(to='app.Group', null=True),
            preserve_default=True,
        ),
    ]
