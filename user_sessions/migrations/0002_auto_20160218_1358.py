# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_sessions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='ip',
            field=models.GenericIPAddressField(verbose_name=b'IP'),
            preserve_default=True,
        ),
    ]
