# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from agenda.models import ItemAgenda #as vezes acontece "do from models import ItemAgenda" Funcionar
from agenda.form import FormItemAgenda
from django.template import RequestContext
from django.http import Http404


def Lista(request):
    lista_itens = ItemAgenda.objects.all()
    return render_to_response("lista.html", {'lista_itens': lista_itens})

def adiciona(request):

    if request.method == "POST":
        form = FormItemAgenda(request.POST, request.FILES)
        if form.is_valid():
            dados = form.cleaned_date
            item = ItemAgenda(
                data=dados['data'],
                hora=dados['hora'],
                titulo=dados['titulo'],
                descricao=dados['descricao'])
            item.save()
            return render_to_response("salvo.html", {})
        else:
             raise Http404
    else:
        form = FormItemAgenda()
        return render_to_response("adiciona.html", {'form': form}, context_instance=RequestContext(request))

