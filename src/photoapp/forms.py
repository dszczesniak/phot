# -*- coding: utf-8 -*-
from django import forms
from datetime import datetime


class SendMessageForm(forms.Form):

	subject = forms.CharField(max_length=30, required=True, label='Temat')
	name = forms.CharField(max_length=40, required=True, label='Imię i nazwisko')
	email = forms.EmailField(required=True, max_length=50, label='E-mail')
	message = forms.CharField(
		widget=forms.Textarea(attrs={'rows': '5', 'cols': '30',}), label='Treść wiadomości', max_length=350, required=True)