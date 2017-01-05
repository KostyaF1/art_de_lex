# -*- coding: utf-8 -*- 
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from page_content.models import PageContent
from nav_bar.models import NavButton, NavLogo
from company.models import Contact, Service, Position, Employee, Company
from feedbacks.forms import FeedbackForm


def index_list(request): 
	main_page = PageContent.objects.get(name='Головна Сторінка')
	#contacts_content = PageContent.objects.get(name='Контакти')
	#services_content = PageContent.objects.get(name='Послуги')
	#feedback_index = PageContent.objects.get(name='Задати Питання')
	nav_buttons = NavButton.objects.all().exclude(url_index = 'feedback').exclude(url_other = 'http://127.0.0.1:8000/')
	nav_feedbacks = NavButton.objects.filter(url_index = 'feedback')
	nav_logo = NavLogo.objects.all()
	company = Company.objects.all()
	if request.method == 'POST':
		feedback_index_form = FeedbackForm(request.POST)
		if feedback_index_form.is_valid():
			feedback = feedback_index_form.save()
			#messages.success(request, u"Course %s has been successfully added." % (feedback.name))
			return redirect('index')
	else:
		feedback_index_form = FeedbackForm()
	return render(request, 'index.html', {
				  'main_page': main_page,
				  'nav_buttons': nav_buttons,
				  'nav_feedbacks': nav_feedbacks,
				  'nav_logo': nav_logo,
                  'company': company,
				  #'feedback_index': feedback_index,
				  'feedback_index_form': feedback_index_form,
				  #'contacts_content': contacts_content,
				  #'services_content': services_content,
                  })
