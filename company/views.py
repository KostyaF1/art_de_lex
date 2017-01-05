# -*- coding: utf-8 -*- 
from django.shortcuts import get_object_or_404, render, redirect
from django.core.exceptions import ObjectDoesNotExist
from company.models import Contact, Service, Position, Employee, Company
from nav_bar.models import NavButton, NavLogo
from page_content.models import PageContent


def employee_detail(request, employees_id):
	nav_buttons = NavButton.objects.all().exclude(url_index = 'feedback').exclude(url_index = '#company')
	nav_feedbacks = NavButton.objects.filter(url_index = 'feedback')
	nav_logo = NavLogo.objects.all()
	try: 
		employee = get_object_or_404(Employee, pk=employees_id)
		company = employee.company_set.all()
		return render(request, 'employees/detail.html', {
                	'employee': employee,
					'company': company,
					'nav_buttons': nav_buttons,
					'nav_feedbacks': nav_feedbacks,
				  	'nav_logo': nav_logo,
                	})
	except ObjectDoesNotExist:
		achtung = "Houston, we have a problem with id = {0} exist yet.".format(employees_id) 
	return render(request, 'employees/detail.html', {
			'achtung': achtung,
			})

def service_detail(request, services_id):
	nav_feedbacks = NavButton.objects.filter(url_index = 'feedback')
	nav_logo = NavLogo.objects.all()
	nav_buttons = NavButton.objects.all().exclude(url_index = 'feedback').exclude(url_index = '#services')
	try: 
		service = get_object_or_404(Service, pk=services_id)
		return render(request, 'services/detail.html', {
                	'service': service,
					'nav_buttons': nav_buttons,
					'nav_feedbacks': nav_feedbacks,
				  	'nav_logo': nav_logo,
                	})
	except ObjectDoesNotExist:
		achtung = "Houston, we have a problem with id = {0} exist yet.".format(services_id) 
	return render(request, 'services/detail.html', {
			"achtung": achtung,
			})

def service_list(request):
	nav_feedbacks = NavButton.objects.filter(url_index = 'feedback')
	nav_logo = NavLogo.objects.all()
	nav_buttons = NavButton.objects.all().exclude(url_index = 'feedback').exclude(url_index = '#services')
	services_content = PageContent.objects.get(name='Послуги')
	services = Service.objects.all()
	return render(request, 'services/list.html', {
                	'services': services,
					"nav_buttons": nav_buttons,
					'services_content': services_content,
					'nav_feedbacks': nav_feedbacks,
				  	'nav_logo': nav_logo,
                	})

