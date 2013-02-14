var divVacios;
var divResultado;
var valor;
var ajax;
function objetoAjax(url, successFun){
	   var xmlhttp=false;
        try {
                xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
        } catch (e) {
                try {
                   xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
                } catch (E) {
                        xmlhttp = false;
                }
        }
        if (!xmlhttp && typeof XMLHttpRequest!='undefined') {
                xmlhttp = new XMLHttpRequest();
        }
        xmlhttp.open('GET', url, true);
        xmlhttp.onreadystatechange=function() {
            if (xmlhttp.readyState==4) {
                successFun( xmlhttp.responseText );
            }
        }
        xmlhttp.send( null );
    }
function ConsultaFiltrado(){	
		var Pag='/buscar';
		divVacios=document.getElementById("Vacios");
		if (document.formulario.q.value==""){
            divVacios.innerHTML ="<div class='mensaje' align='justify'>Complete la informacion</div>"
        }
        else{
		divResultado = document.getElementById("resultado");
		valor=document.formulario.q.value;
		objetoAjax(Pag+"?q="+valor,function(respuesta){
             divResultado.innerHTML = respuesta;
             divVacios.innerHTML = "";
        });       
		}
}

function insertar(Pag,objId,objIdVacio) {
        divVacios=document.getElementById(objIdVacio);
        if (document.formulario.nom.value=="" || document.formulario.ape.value=="" || document.formulario.pais.value=="" || document.formulario.correo.value=="")
        {
            divVacios.innerHTML ="<div class='mensaje' align='justify'>Complete la informacion</div>"
        }
        else{
		divResultado = document.getElementById(objId);
        nombre=document.formulario.nom.value;
        direccion=document.formulario.ape.value;
        web=document.formulario.pais.value;
        idioma=document.formulario.correo.value;
        pais=document.formulario.correo.value;

        objetoAjax(Pag+"?nombre="+nombre+"&direccion="+direccion+"&web="+web+"&idioma="+idioma+"&pais="+pais,function(respuesta){
             divResultado.innerHTML = respuesta;
             divVacios.innerHTML = "";
        });       
		}      
}
function eliminar(Pag,objId,idEliminar) {
		divResultado = document.getElementById(objId);
		var agree=confirm('Eliminar el registro #'+idEliminar+'?');
		if (agree){
			 objetoAjax(Pag,function(respuesta){
             divResultado.innerHTML = respuesta;
             divVacios.innerHTML = "";
        });       
		}		
}
function detalle_actualizar(Pag,objId,idActualizar) {
		divResultado = document.getElementById(objId);
		var agree=confirm('Actualizar el registro #'+idActualizar+'?');
		if (agree){
			objetoAjax(Pag,function(respuesta){
             divResultado.innerHTML = respuesta;
             divVacios.innerHTML = "";
        }); 			
		}	
}
function actualizar(Pag,objId,objIdVacio) {
        divVacios=document.getElementById(objIdVacio);
        if (document.formulario.nom.value=="" || document.formulario.ape.value=="" || document.formulario.pais.value=="" || document.formulario.correo.value=="")
        {
            divVacios.innerHTML ="<div class='mensaje' align='justify'>Complete la informacion</div>";
        }
        else
        {
		divResultado = document.getElementById(objId);
		id=document.formulario.id.value;
        nom=document.formulario.nom.value;
        ape=document.formulario.ape.value;
        pais=document.formulario.pais.value;
        correo=document.formulario.correo.value;
        objetoAjax(Pag+"?id="+id+"&nom="+nom+"&ape="+ape+"&pais="+pais+"&correo="+correo,function(respuesta){
        divResultado.innerHTML = respuesta;
        divVacios.innerHTML = "";
        }); 
      }
}



