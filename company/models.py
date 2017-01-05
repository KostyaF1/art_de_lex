# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import RegexValidator
from ckeditor_uploader.fields import RichTextUploadingField


class Contact(models.Model):
	city = models.CharField(
    	max_length=70, verbose_name = u'Город*')
	street = models.CharField(
    	max_length=70, blank = True, verbose_name = u'Вулиця')
	full_adress = RichTextUploadingField(
    	blank = True, verbose_name = u'Повна Адреса')
	mobile_number1 = RegexValidator(regex=r'^\+?1?\d{10,13}$',
		message="Номер мобильного должен быть в следующем формате: '+380XXXXXXXXX'. До 13 символов.")
	mobile_number2 = RegexValidator(regex=r'^\+?1?\d{10,13}$',
		message="Номер мобильного должен быть в следующем формате: '+380XXXXXXXXX'. До 13 символов.")
	mobile_number3 = RegexValidator(regex=r'^\+?1?\d{10,13}$',
		message="Номер мобильного должен быть в следующем формате: '+380XXXXXXXXX'. До 13 символов.")
	mobile_number4 = RegexValidator(regex=r'^\+?1?\d{10,13}$',
		message="Номер мобильного должен быть в следующем формате: '+380XXXXXXXXX'. До 13 символов.")
	phone_regex = RegexValidator(regex=r'^\+?1?\d{10,13}$',
		message="Номер телефона должен быть в следующем формате: '+38057XXXXXXX'. До 13 символов.")
	email = models.EmailField()
	photo = models.ImageField(
    	upload_to='pictures', verbose_name = u'Изображение', blank = True)
    
	def __unicode__(self):
		return self.street

class Service(models.Model):
	name = RichTextUploadingField(max_length=200, verbose_name = u"Наименование Услуги")
	description = RichTextUploadingField()
	url = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.name

class Position(models.Model):
	name = RichTextUploadingField(max_length = 20, verbose_name = u"Должность", blank = True)
	
	def __unicode__(self):
		return self.name 

class Employee(models.Model):
	first_name = RichTextUploadingField(max_length = 15, verbose_name = u"Имя")
	last_name = RichTextUploadingField(max_length = 15, verbose_name = u"Фамилия")
	date_of_birth = models.DateField(verbose_name = u"Дата Рождения")
	gender = RichTextUploadingField(max_length = 15, choices = (("Male", u"Мужской"),
		("Female", u"Женский")), verbose_name = u"Пол")
	position = models.ForeignKey(Position)
	biography = RichTextUploadingField(verbose_name = u"Биография")
	photo = RichTextUploadingField(
    	verbose_name = u'Изображение', blank = True)

	def get_full_name(self):
		return self.first_name + " " + self.last_name
	
	def __unicode__(self):
		return self.first_name + " " + self.last_name

class Company(models.Model):
	name = RichTextUploadingField(max_length = 15, verbose_name = u"Компания", blank = True)
	description = RichTextUploadingField(verbose_name = u"Описание")
	employees = models.ManyToManyField(Employee, verbose_name = u"Сотрудники")
	services = models.ManyToManyField(Service)
	contacts = models.ForeignKey(Contact)
	
	def __unicode__(self):
		return self.name
