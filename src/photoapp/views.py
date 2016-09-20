# -*- coding: utf-8 -*-
import os
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from .forms import SendMessageForm
from datetime import datetime

def home(request):


	return render(request, "home.html", {})



def contact(request):

	form = SendMessageForm(request.POST or None)

	if form.is_valid():
		human = True
		form_message = form.cleaned_data.get("message")
		subject = form.cleaned_data.get("subject")
		name = form.cleaned_data.get("name")
		email = form.cleaned_data.get("email")

		from_emial = settings.EMAIL_HOST_USER

		start = 'Wiadomosc od: '+name+', e-mail: '+email
		end = "--- Koniec ---"

		to_email = ['dszczesniak@poczta.pl']

		contact_message = "%s \n\n%s \n\n %s" %(start, form_message, end)

		send_mail(subject, contact_message, from_emial, to_email, fail_silently=True)
		messages.success(request, 'Dziękuję za wiadomość. Postaram się odpowiedzieć jak najszybciej :)')
		return redirect('/contact', {})

	con = {
		"form": form,
	}

	return render(request, "contact.html", con)



def portfolio(request):


	return render(request, "portfolio.html", {})

def me(request):
	
	return render(request, "about_me.html", {})

