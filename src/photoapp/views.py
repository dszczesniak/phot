# -*- coding: utf-8 -*-
import os
import warnings
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
from django.views.generic.list import ListView
from photologue.models import Gallery
import warnings
from django.views.generic.dates import ArchiveIndexView, DateDetailView, DayArchiveView, MonthArchiveView, YearArchiveView
from django.views.generic.detail import DetailView

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

	return render(request, "kontakt.html", con)



def portfolio(request):


	return render(request, "portfolio.html", {})

def me(request):
	
	return render(request, "o_mnie.html", {})


def sessions_pregnancy_view(request):
	queryset = Gallery.objects.on_site().is_public()
	paginate_by = 5

	return render(request, "sesje_ciazowe.html", {"queryset": queryset})


def sessions_neonatal_view(request):
	queryset = Gallery.objects.on_site().is_public()
	paginate_by = 5

	return render(request, "sesje_noworodkowe.html", {"queryset": queryset})

def sessions_family_view(request):
	queryset = Gallery.objects.on_site().is_public()
	paginate_by = 5

	return render(request, "sesje_rodzinne.html", {"queryset": queryset})

def sessions_occasional_view(request):
	queryset = Gallery.objects.on_site().is_public()
	paginate_by = 5

	return render(request, "sesje_okazjonalne.html", {"queryset": queryset})

def project_360_view(request):
	queryset = Gallery.objects.on_site().is_public()
	paginate_by = 5

	return render(request, "projekt_360.html", {"queryset": queryset})