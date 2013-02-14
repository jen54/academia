#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

#class Ubicacion(models.Model):
 #   nombre =  models.CharField(max_length=200, help_text='Nombre', verbose_name='Nombre')
  #  usuario = models.ForeignKey(User)

    #def __unicode__(self):
     #   return self.nombre


class Continente(models.Model):
    nombre=  models.CharField(max_length=200, verbose_name='Nombre Continente')
    #cod_continente=  models.CharField(max_length=200, verbose_name='Código Continente')
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.nombre


class Pais(models.Model):
    nombre_pais =  models.CharField(max_length=200, verbose_name='Nombre Pais')
    continente = models.ForeignKey(Continente)

    def __unicode__(self):
        return self.nombre_pais


class Ciudad(models.Model):
    nombre_ciudad =  models.CharField(max_length=200, verbose_name='Nombre Ciudad')
    pais = models.ForeignKey(Pais)
    continente = models.ForeignKey(Continente)


    def __unicode__(self):
        return self.nombre_ciudad


class Universidad(models.Model):
	nombre= models.CharField(max_length=100, verbose_name='Nombre', unique=True)
	direccion= models.CharField(max_length=100, verbose_name='Dirección', unique=True)
	web= models.CharField(max_length=100, verbose_name='Web', unique=True)
	#imagen = models.ImageField(upload_to='universidades', verbose_name='Imágen')
	#informacion = models.TextField(verbose_name='Informacion')
	#mail = models.TextField(verbose_name='E-mail')
	idioma= models.CharField(max_length=100, verbose_name='Idioma', unique=False)

	usuario = models.ForeignKey(User)
        continente = models.ForeignKey(Continente)
        pais = models.ForeignKey(Pais)
        ciudad = models.ForeignKey(Ciudad)
	
	def __unicode__(self):
		return self.nombre

class Comentario(models.Model):
    universidad = models.ForeignKey(Universidad)
    texto = models.TextField(help_text='Tu comentario', verbose_name='Comentario')

    def __unicode__(self):
        return self.texto
