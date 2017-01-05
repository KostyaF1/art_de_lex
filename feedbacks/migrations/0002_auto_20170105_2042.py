# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='phone',
            field=models.CharField(default='+380000000000', max_length=100, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0412\u0430\u0448\u043e\u0433\u043e \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0443'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='callorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0437\u043c\u0456\u0449\u0435\u043d\u043d\u044f'),
        ),
        migrations.AlterField(
            model_name='callorder',
            name='name',
            field=models.CharField(max_length=100, verbose_name='\u0424.\u0406.\u041e.'),
        ),
        migrations.AlterField(
            model_name='callorder',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0412\u0430\u0448\u043e\u0433\u043e \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0443'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0437\u043c\u0456\u0449\u0435\u043d\u043d\u044f'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='from_email',
            field=models.EmailField(max_length=75, verbose_name='\u0412\u0430\u0448 e-mail'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(verbose_name='\u041f\u0438\u0442\u0430\u043d\u043d\u044f'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=225, verbose_name='\u0424.\u0406.\u041e.'),
        ),
    ]
