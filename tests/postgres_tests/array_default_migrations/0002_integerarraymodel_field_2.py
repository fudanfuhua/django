# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postgres_tests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='integerarraymodel',
            name='field_2',
            field=django.contrib.postgres.fields.ArrayField(models.IntegerField(), default=[], size=None),
            preserve_default=False,
        ),
    ]
