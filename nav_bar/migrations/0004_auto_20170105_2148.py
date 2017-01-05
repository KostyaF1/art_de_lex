# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nav_bar', '0003_auto_20170105_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbutton',
            name='alias',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='adl', verbose_name='\u041f\u043e\u043b\u0454 \u043d\u0430 \u0441\u0442\u043e\u0440\u0456\u043d\u0446\u0456', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='navlogo',
            name='alias',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041f\u043e\u043b\u0454 \u043d\u0430 \u0441\u0442\u043e\u0440\u0456\u043d\u0446\u0456', blank=True),
        ),
    ]
