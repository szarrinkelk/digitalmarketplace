# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_sal_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sal_price',
            new_name='sale_price',
        ),
    ]
