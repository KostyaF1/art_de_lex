# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class PageContent(models.Model):
	name = models.CharField(
    	max_length=200, verbose_name = u'Наименование раздела*')
	description = RichTextUploadingField(blank = True, verbose_name = u'Описание раздела*')
	field1 = RichTextUploadingField(
    	max_length=250, blank = True, verbose_name = u'Поле1')
	field2 = RichTextUploadingField(
    	max_length=250, blank = True, verbose_name = u'Поле2')
	field3 = RichTextUploadingField(
    	max_length=250, blank = True, verbose_name = u'Поле3')
	field4 = RichTextUploadingField(
    	max_length=250, blank = True, verbose_name = u'Поле4')
	photo = models.ImageField(
    	upload_to='pictures', verbose_name = u'Изображение', blank = True)
    
	def __unicode__(self):
		return self.name
