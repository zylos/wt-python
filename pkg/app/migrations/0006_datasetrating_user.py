# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_auto_20141225_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasetrating',
            name='user',
            field=models.ForeignKey(related_name='ratings', default=9999, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
