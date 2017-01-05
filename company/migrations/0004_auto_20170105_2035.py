# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20170105_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='mobile_number1',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='+380000000000', max_length=100, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u041c\u043e\u0431\u0456\u043b\u044c\u043d\u043e\u0433\u043e1', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='mobile_number2',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='+380000000000', max_length=100, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u041c\u043e\u0431\u0456\u043b\u044c\u043d\u043e\u0433\u043e2', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='mobile_number3',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='+380000000000', max_length=100, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u041c\u043e\u0431\u0456\u043b\u044c\u043d\u043e\u0433\u043e3', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='mobile_number4',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='+380000000000', max_length=100, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u041c\u043e\u0431\u0456\u043b\u044c\u043d\u043e\u0433\u043e4', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_regex',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='+380000000000', max_length=100, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0422\u0435\u043b\u0435\u0444\u043e\u043d\u0443', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='name',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='name', verbose_name='\u041f\u043e \u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name="\u0406\u043c'\u044f", blank=True),
        ),
    ]
