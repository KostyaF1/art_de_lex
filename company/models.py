# -*- coding: utf-8 -*-
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Contact(models.Model):
	city = models.CharField(
    	max_length=70, verbose_name = u'Місто*')
	street = models.CharField(
    	max_length=70, blank = True, verbose_name = u'Вулиця')
	full_adress = RichTextUploadingField(
    	blank = True, verbose_name = u'Повна Адреса')
	mobile_number1 = RichTextUploadingField(verbose_name = u"Номер Мобільного1", blank = True, max_length=100)
	mobile_number2 = RichTextUploadingField(verbose_name = u"Номер Мобільного2", blank = True, max_length=100)
	mobile_number3 = RichTextUploadingField(verbose_name = u"Номер Мобільного3", blank = True, max_length=100)
	mobile_number4 = RichTextUploadingField(verbose_name = u"Номер Мобільного4", blank = True, max_length=100)
	phone_regex = RichTextUploadingField(verbose_name = u"Номер Телефону", blank = True, max_length=100)
	email = models.EmailField()
	photo = models.ImageField(
    	upload_to='pictures', verbose_name = u'Зображення', blank = True)
    
	def __unicode__(self):
		return self.street


class Service(models.Model):
	name = RichTextUploadingField(verbose_name = u"Назва Послуги", blank = True)
	description = RichTextUploadingField(verbose_name = u"Опис Послуги", blank = True)
	url = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.name


class Position(models.Model):
	name = RichTextUploadingField(verbose_name = u"Посада", blank = True)
	
	def __unicode__(self):
		return self.name 


class Employee(models.Model):
	first_name = RichTextUploadingField(verbose_name = u"Ім'я", blank = True)
	name = RichTextUploadingField(verbose_name = u"По батькові", blank = True)
	last_name = RichTextUploadingField(verbose_name = u"Призвище", blank = True)
	date_of_birth = models.DateField(verbose_name = u"Дата Народження", blank = True)
	gender = models.CharField(max_length=15, choices = (("Male", u"Мужской"),
		("Female", u"Жіночий")), verbose_name = u"Чоловічий")
	position = models.ForeignKey(Position)
	biography = RichTextUploadingField(verbose_name = u"Біографія", blank = True)
	photo = RichTextUploadingField(
    	verbose_name = u'Зображення', blank = True)

	def get_full_name(self):
		return self.first_name + " " + self.last_name
	
	def __unicode__(self):
		return self.first_name + " " + self.last_name


class Company(models.Model):
	name = RichTextUploadingField(verbose_name = u"Назва Компанії", blank = True)
	description = RichTextUploadingField(verbose_name = u"Опис", blank = True)
	employees = models.ManyToManyField(Employee, verbose_name = u"Співробітники")
	services = models.ManyToManyField(Service, verbose_name = u"Послуги")
	contacts = models.ForeignKey(Contact, verbose_name = u"Контакти")
	
	def __unicode__(self):
		return self.name
