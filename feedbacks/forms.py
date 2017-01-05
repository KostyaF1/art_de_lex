# -*- coding: utf-8 -*- 
from django import forms
from feedbacks.models import Feedback, CallOrder

class FeedbackForm(forms.ModelForm):
	'''error_css_class = 'class-error'
	required_css_class = 'class-required'''
	class Meta:
		model = Feedback
		fields = [ 'name', 'subject', 'message', 'from_email' ]
	'''def __init__(self, *args, **kwargs):
		super(forms.ModelForm, self).__init__(*args, **kwargs)
        # adding css classes to widgets without define the fields:
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'some-class other-class'
	def as_div(self):
		return self._html_output(
			normal_row = u'<div%(html_class_attr)s>%(label)s %(field)s %(help_text)s %(errors)s</div>',
			error_row = u'<div class="error">%s</div>',
			row_ender = '</div>',
			help_text_html = u'<div class="hefp-text">%s</div>',
			errors_on_separate_row = False)'''

class CallOrderForm(forms.ModelForm):
	class Meta:
		model = CallOrder
		fields = [ 'name', 'subject', 'phone']
