# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.mail import mail_admins
from feedbacks.models import Feedback, CallOrder
from feedbacks.forms import FeedbackForm, CallOrderForm


class FeedbackView(CreateView):
	model = Feedback
	template_name = 'feedback.html'
	form_class = FeedbackForm
	context_object_name = 'form'
	success_url = reverse_lazy('index')
    #success_message = u"Thank you for your feedback! We will keep in touch with you very soon!"
    
	def get_context_data(self, **kwargs):
		context = super(FeedbackView, self).get_context_data(**kwargs)
		context['title'] = "Обратная связь"
		return context 

	def form_valid(self, form):
		feedback = form.save()
		messages.success(self.request, u"Спасибо за Ваше сообщение! Наш менеджер перезвонит Вам!")
		mail_admins(feedback.subject, feedback.message)
		return super(FeedbackView, self).form_valid(form)

class CallOrderView(CreateView):
    model = CallOrder
    template_name = 'call_order.html'
    form_class = CallOrderForm
    context_object_name = 'form'
    success_url = reverse_lazy('coopiration')
    
    def get_context_data(self, **kwargs):
        context = super(CallOrderView, self).get_context_data(**kwargs)
        context['title'] = "Заказать звонок"
        return context 

    def form_valid(self, form):
        call_order = form.save()
        messages.success(self.request, u"Спасибо за Ваше сообщение! Наш менеджер перезвонит Вам!")
        mail_admins(call_order.name, call_order.phone, call_order.message)
        return super(CallOrderView, self).form_valid(form)
