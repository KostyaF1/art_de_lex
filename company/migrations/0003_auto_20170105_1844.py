# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20170105_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='contacts',
            field=models.ForeignKey(verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u0438', to='company.Contact'),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041e\u043f\u0438\u0441', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='employees',
            field=models.ManyToManyField(to=b'company.Employee', verbose_name='\u0421\u043f\u0456\u0432\u0440\u043e\u0431\u0456\u0442\u043d\u0438\u043a\u0438'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041d\u0430\u0437\u0432\u0430 \u041a\u043e\u043c\u043f\u0430\u043d\u0456\u0457', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='services',
            field=models.ManyToManyField(to=b'company.Service', verbose_name='\u041f\u043e\u0441\u043b\u0443\u0433\u0438'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(max_length=70, verbose_name='\u041c\u0456\u0441\u0442\u043e*'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='photo',
            field=models.ImageField(upload_to=b'pictures', verbose_name='\u0417\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='biography',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u0411\u0456\u043e\u0433\u0440\u0430\u0444\u0456\u044f', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u041d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041f\u043e \u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(max_length=15, verbose_name='\u0427\u043e\u043b\u043e\u0432\u0456\u0447\u0438\u0439', choices=[(b'Male', '\u041c\u0443\u0436\u0441\u043a\u043e\u0439'), (b'Female', '\u0416\u0456\u043d\u043e\u0447\u0438\u0439')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041f\u0440\u0438\u0437\u0432\u0438\u0449\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u0417\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f', blank=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='name',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041f\u043e\u0441\u0430\u0434\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041e\u043f\u0438\u0441 \u041f\u043e\u0441\u043b\u0443\u0433\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041d\u0430\u0437\u0432\u0430 \u041f\u043e\u0441\u043b\u0443\u0433\u0438', blank=True),
        ),
    ]
