# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nav_bar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbutton',
            name='name',
            field=models.CharField(max_length=20, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u043a\u043d\u043e\u043f\u043a\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='navlogo',
            name='name',
            field=models.CharField(max_length=20, verbose_name='\u041f\u043e\u043b\u0454 \u043d\u0430 \u0441\u0442\u043e\u0440\u0456\u043d\u0446\u0456', blank=True),
        ),
    ]
