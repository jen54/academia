from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
	 url(r'^$','principal.views.inicio'),
    url(r'^usuarios/$','principal.views.usuarios'),
    #url(r'^sobre/$','principal.views.sobre'),
    url(r'^universidades/$','principal.views.lista_universidades'),
    url(r'^universidad/(?P<id_universidad>\d+)$','principal.views.detalle_universidad'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
    url(r'^contacto/$','principal.views.contacto'),

    url(r'^comenta/$','principal.views.nuevo_comentario'),
    url(r'^usuario/nuevo$','principal.views.nuevo_usuario'),
    url(r'^ingresar/$','principal.views.ingresar'),
    url(r'^privado/$','principal.views.privado'),
    url(r'^cerrar/$', 'principal.views.cerrar'),

    url(r'^buscar/$', 'principal.views.consulta'),

        url(r'^gestion/$','principal.views.gestion'),
    url(r'^add/$','principal.views.agregar_universidad'),
    url(r'^borrar/(?P<id_universidad>\d+)$','principal.views.eliminar'),
    url(r'^editar/(?P<id_universidad>\d+)$','principal.views.editar'),
    url(r'^add_user_ajax/$', 'principal.views.agregar_universidad_ajax'),
    url(r'^editar_ajax/$', 'principal.views.editar_ajax'),
        url(r'media/(?P<path>.*)', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),

    url(r'^combo/$','principal.views.combo'),
    url(r'^combo_ciudad/$','principal.views.combo1'), 
    url(r'^combo_continente/$','principal.views.combo2'), 

    url(r'^json/$', 'principal.views.json_universidad'),
)
