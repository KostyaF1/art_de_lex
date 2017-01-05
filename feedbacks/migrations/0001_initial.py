# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u0424.\u0418.\u041e.')),
                ('subject', models.CharField(max_length=100, verbose_name='\u0422\u0435\u043c\u0430')),
                ('phone', models.IntegerField(max_length=100, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0412\u0430\u0448\u0435\u0433\u043e \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0430\u0437\u043c\u0435\u0449\u0435\u043d\u0438\u044f')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=225, verbose_name='\u0424.\u0418.\u041e.')),
                ('subject', models.CharField(max_length=255, verbose_name='\u0422\u0435\u043c\u0430')),
                ('message', models.TextField(verbose_name='\u041f\u043e \u0434\u0435\u043b\u0443')),
                ('from_email', models.EmailField(max_length=75)),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0430\u0437\u043c\u0435\u0449\u0435\u043d\u0438\u044f ')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
