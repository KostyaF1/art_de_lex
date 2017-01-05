# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', ckeditor_uploader.fields.RichTextUploadingField(max_length=15, verbose_name='\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u044f', blank=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=70, verbose_name='\u0413\u043e\u0440\u043e\u0434*')),
                ('street', models.CharField(max_length=70, verbose_name='\u0412\u0443\u043b\u0438\u0446\u044f', blank=True)),
                ('full_adress', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041f\u043e\u0432\u043d\u0430 \u0410\u0434\u0440\u0435\u0441\u0430', blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('photo', models.ImageField(upload_to=b'pictures', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', ckeditor_uploader.fields.RichTextUploadingField(max_length=15, verbose_name='\u0418\u043c\u044f')),
                ('last_name', ckeditor_uploader.fields.RichTextUploadingField(max_length=15, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('date_of_birth', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0420\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('gender', ckeditor_uploader.fields.RichTextUploadingField(max_length=15, verbose_name='\u041f\u043e\u043b', choices=[(b'Male', '\u041c\u0443\u0436\u0441\u043a\u043e\u0439'), (b'Female', '\u0416\u0435\u043d\u0441\u043a\u0438\u0439')])),
                ('biography', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u0411\u0438\u043e\u0433\u0440\u0430\u0444\u0438\u044f')),
                ('photo', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', ckeditor_uploader.fields.RichTextUploadingField(max_length=20, verbose_name='\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', ckeditor_uploader.fields.RichTextUploadingField(max_length=200, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0423\u0441\u043b\u0443\u0433\u0438')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('url', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(to='company.Position'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='contacts',
            field=models.ForeignKey(to='company.Service'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='employees',
            field=models.ManyToManyField(to='company.Employee', verbose_name='\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='services',
            field=models.ManyToManyField(to='company.Contact'),
            preserve_default=True,
        ),
    ]
