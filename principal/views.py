from principal.models import Universidad, Comentario, Continente, Ciudad, Pais
from principal.forms import UniversidadForm, ComentarioForm, ContactoForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import  Http404
from django.utils import simplejson as json
from django.core import serializers


def inicio(request):
    universidades = Universidad.objects.all()
    return render_to_response('inicio.html',{'universidades':universidades}, context_instance=RequestContext(request))

def usuarios(request):
    usuarios = User.objects.all()
    universidades = Universidad.objects.all()
    return render_to_response('usuarios.html',{'usuarios':usuarios,'universidades':universidades}, context_instance=RequestContext(request))

def lista_universidades(request):
    universidades = Universidad.objects.all()
    return render_to_response('universidades.html',{'datos':universidades}, context_instance=RequestContext(request))

def detalle_universidad(request, id_universidad):
    dato = get_object_or_404(Universidad, pk=id_universidad)
    comentarios = Comentario.objects.filter(universidad=dato)
    return render_to_response('universidad.html',{'universidad':dato,'comentarios':comentarios}, context_instance=RequestContext(request))
#---------------------------------------------------------------------------
def gestion(request):
    universidades = Universidad.objects.all()
    return render_to_response('index.html',{'universidades':universidades},context_instance=RequestContext(request))

def agregar_universidad(request):
    formulario = UniversidadForm()
    return render_to_response("agregar_universidad.html",{'formulario':formulario},context_instance=RequestContext(request))

def agregar_universidad_ajax(request):
    if request.is_ajax() and request.method == 'POST':
        formulario = UniversidadForm(request.POST, request.FILES)
        errores = ''
        exito = False
        if formulario.is_valid():
            formulario.save()
            exito = True
        else:
            errores = formulario.errors
        response = {'exito':exito, 'errores':errores}
        return HttpResponse(json.dumps(response), mimetype="application/json")
    else:
        raise Http404

def eliminar(request,id_universidad):
    universidad = Universidad.objects.get(pk=id_universidad)
    universidad.delete()
    return HttpResponseRedirect("/")

def editar(request,id_universidad):
    universidad = Universidad.objects.get(pk=id_universidad)
    formulario = UniversidadForm(instance=universidad)
    return render_to_response("editar_universidad.html",{'formulario':formulario},context_instance=RequestContext(request))

def editar_ajax(request):
    if request.is_ajax() and request.method == 'POST':
        universidad = Universidad.objects.get(pk=request.POST['id_universidad'])
        formulario = UniversidadForm(request.POST, request.FILES, instance=universidad)
        errores = ''
        exito = False
        if formulario.is_valid():
            formulario.save()
            exito = True
        else:
            errores = formulario.errors
        response = {'exito':exito, 'errores':errores}
        return HttpResponse(json.dumps(response), mimetype="application/json")
    else:
        raise Http404




#------------------------------------------------------
################################################################################
# def inicio(request):
#     universidades = Universidad.objects.all()
#     consulta = request.GET.get('q', '') 
#     if consulta:         
#         results=Universidad.objects.filter(nombre=consulta).order_by('id')
#         return render_to_response("inicio.html", { "results": results,"consulta": consulta})  
#     return render_to_response("inicio.html", { "results": [],"consulta": consulta})   
#     return render_to_response('inicio.html',{'universidades':universidades}, context_instance=RequestContext(request))

def consulta(request):
    consulta = request.GET.get('q', '') 
    if consulta:         
        results=Universidad.objects.filter(nombre=consulta).order_by('id')
        return render_to_response("inicio.html", { "results": results,"consulta": consulta})  
    return render_to_response("inicio.html", { "results": [],"consulta": consulta})           
#############################################################################
def combo(request):
    query = request.GET.get('q', '') 
    elementos= Pais.objects.all()
    if query:
        results=Universidad.objects.filter(pais=query)
        return render_to_response("consulta_combo.html",{"results": results,"query": query,"elementos": elementos}, context_instance=RequestContext(request) )
    return render_to_response("consulta_combo.html",{"results": elementos,"query":  query,"elementos": elementos}, context_instance=RequestContext(request))         

################################################################################
def combo1(request):
    query = request.GET.get('q', '') 
    elementos= Ciudad.objects.all()
    if query:
        results=Universidad.objects.filter(ciudad=query)
        return render_to_response("consulta_ciudad.html",{"results": results,"query": query,"elementos": elementos}, context_instance=RequestContext(request) )
    return render_to_response("consulta_ciudad.html",{"results": elementos,"query":  query,"elementos": elementos}, context_instance=RequestContext(request))         
################################################################################

################################################################################
def combo2(request):
    query = request.GET.get('q', '') 
    elementos= Continente.objects.all()
    # elementos= Universidad.objects.values('pais','').distinct()
    if query:
        results=Universidad.objects.filter(continente=query)
        return render_to_response("consulta_continente.html",{"results": results,"query": query,"elementos": elementos}, context_instance=RequestContext(request) )
    return render_to_response("consulta_continente.html",{"results": elementos,"query":  query,"elementos": elementos}, context_instance=RequestContext(request))         
################################################################################


def contacto(request):
    if request.method=='POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje desde el recetario de Maestros del Web'
            contenido = formulario.cleaned_data['mensaje'] + "\n"
            contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['destinatario@email.com'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
        formulario = ContactoForm()
    return render_to_response('contactoform.html',{'formulario':formulario}, context_instance=RequestContext(request))


def nuevo_comentario(request):
    if request.method=='POST':
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/universidades')
    else:
        formulario = ComentarioForm()
    return render_to_response('comentarioform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def nuevo_usuario(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render_to_response('nuevousuario.html',{'formulario':formulario}, context_instance=RequestContext(request))

def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/privado')
                else:
                    return render_to_response('noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def privado(request):
    usuario = request.user
    return render_to_response('privado.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')

def json_universidad(request):
    data = serializers.serialize("json",Universidad.objects.all())
    return HttpResponse(data,mimetype='aplication/json')
