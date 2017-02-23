# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(default=9.99, max_digits=100, decimal_places=2),
            preserve_default=True,
        ),
    ]
