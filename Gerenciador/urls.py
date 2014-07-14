from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Gerenciador.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', "agenda.views.Lista"),
    url(r'^adiciona', "agenda.views.adiciona")
)
