__author__ = 'rp-leal'

from django import forms

class FormItemAgenda(forms.Form):

    data = forms.DateField()
    hora = forms.TimeField()
    titulo = forms.CharField(max_length="100")
    descricao = forms.TimeField()


