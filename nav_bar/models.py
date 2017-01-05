# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

class NavButton(models.Model):
	name = models.CharField(
        max_length=20, verbose_name = u"Наименование", blank = True)
	url_index = models.CharField(
        max_length=50, null = True, blank = True)
	url_other = models.CharField(
        max_length=50, null = True, blank = True)

	def __unicode__(self):
		return self.name

class NavLogo(models.Model):
	name = models.CharField(
        max_length=20, verbose_name = u"Наименование", blank = True)
	url_index = models.CharField(
        max_length=50, null = True, blank = True)
	url_other = models.CharField(
        max_length=50, null = True, blank = True)

	def __unicode__(self):
		return self.name
