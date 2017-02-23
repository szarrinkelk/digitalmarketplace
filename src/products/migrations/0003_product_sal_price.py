# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20170110_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sal_price',
            field=models.DecimalField(default=6.99, null=True, max_digits=100, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
