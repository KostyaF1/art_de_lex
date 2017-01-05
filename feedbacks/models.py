# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User
import datetime


class Feedback(models.Model):
	name = models.CharField( max_length=225, verbose_name=u'Ф.І.О.')
	subject = models.CharField(max_length=255, verbose_name=u'Тема')
	message = models.TextField(verbose_name=u'Питання')
	phone = models.CharField(max_length=100, verbose_name=u'Номер Вашого телефону')
	from_email = models.EmailField(verbose_name=u'Ваш e-mail')
	date = models.DateTimeField(default = datetime.datetime.now, verbose_name=u'Дата розміщення')

	def __unicode__(self):
		return self.subject

class CallOrder(models.Model):
	name = models.CharField( max_length=100, verbose_name=u'Ф.І.О.')
	subject = models.CharField(max_length=100, verbose_name=u'Тема')
	phone = models.CharField(max_length=100, verbose_name=u'Номер Вашого телефону')
	date = models.DateTimeField(default = datetime.datetime.now, verbose_name=u'Дата розміщення')

	def __unicode__(self):
		return self.subject
