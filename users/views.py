from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

from .forms import NameForm, ContactForm


def get_name(request):
	template_name = 'users/name.html'
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			HttpResponse('/thanks/')
	else:
		form = NameForm()
		context = {'form': form}
		return render(request, template_name, context)


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']

			recipients = ['email@example.com']
			if cc_myself:
				recipients.append(recipients)

			send_mail(subject, message, sender, recipients)
			return HttpResponse('/thanks/')

	else:
		form = ContactForm()
		context = {'form': form}
		template_name = 'users/contact.html'
		return render(request, template_name, context)
