# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('uuid', uuidfield.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=32, blank=True, unique=True)),
                ('title', models.CharField(max_length=32)),
                ('url_name', models.CharField(max_length=32)),
                ('version', models.CharField(max_length=32)),
                ('url', models.URLField(max_length=256)),
                ('notes', models.TextField()),
                ('set_type', models.CharField(default=b'dataset', max_length=32, choices=[(b'dataset', b'Data Set'), (b'unknown', b'Unknown')])),
                ('is_private', models.BooleanField(default=False)),
                ('is_open', models.BooleanField(default=False)),
                ('activity_state', models.CharField(default=b'inactive', max_length=32, choices=[(b'inactive', b'Inactive'), (b'pending', b'Pending'), (b'active', b'Active')])),
                ('created_on', models.DateTimeField()),
                ('modified_on', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataSetExtra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('content', models.TextField()),
                ('dataset', models.ForeignKey(to='app.DataSet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataSetRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.FloatField()),
                ('dataset', models.ForeignKey(to='app.DataSet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataSetResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.PositiveIntegerField()),
                ('dataset', models.ForeignKey(to='app.DataSet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('uuid', uuidfield.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=32, blank=True, unique=True)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32)),
                ('license_type', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('uuid', uuidfield.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=32, blank=True, unique=True)),
                ('url', models.URLField(max_length=255)),
                ('name', models.CharField(max_length=32)),
                ('desc', models.TextField()),
                ('created_on', models.DateTimeField()),
                ('modified_on', models.DateTimeField()),
                ('file_size', models.PositiveIntegerField()),
                ('file_hash', models.CharField(max_length=32)),
                ('file_type', models.CharField(max_length=32)),
                ('file_mimetype', models.CharField(max_length=32)),
                ('file_format', models.CharField(max_length=32)),
                ('group', models.ForeignKey(to='app.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='datasetresource',
            name='resource',
            field=models.ForeignKey(to='app.Resource'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dataset',
            name='resources',
            field=models.ManyToManyField(to='app.Resource', through='app.DataSetResource'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dataset',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
            preserve_default=True,
        ),
    ]
