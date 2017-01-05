# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='contacts',
            field=models.ForeignKey(to='company.Contact'),
        ),
        migrations.AlterField(
            model_name='company',
            name='services',
            field=models.ManyToManyField(to=b'company.Service'),
        ),
    ]
