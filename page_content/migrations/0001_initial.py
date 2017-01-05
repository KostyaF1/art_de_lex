# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0440\u0430\u0437\u0434\u0435\u043b\u0430*')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0440\u0430\u0437\u0434\u0435\u043b\u0430*', blank=True)),
                ('field1', ckeditor_uploader.fields.RichTextUploadingField(max_length=250, verbose_name='\u041f\u043e\u043b\u04351', blank=True)),
                ('field2', ckeditor_uploader.fields.RichTextUploadingField(max_length=250, verbose_name='\u041f\u043e\u043b\u04352', blank=True)),
                ('field3', ckeditor_uploader.fields.RichTextUploadingField(max_length=250, verbose_name='\u041f\u043e\u043b\u04353', blank=True)),
                ('field4', ckeditor_uploader.fields.RichTextUploadingField(max_length=250, verbose_name='\u041f\u043e\u043b\u04354', blank=True)),
                ('photo', models.ImageField(upload_to=b'pictures', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
