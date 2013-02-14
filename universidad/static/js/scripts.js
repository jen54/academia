/*____________________________________________________________________*/
function confirmar(vartext)
{
var agree=confirm(vartext);
if (agree)
	return true ;
else
	return false ;
}
/*____________________________________________________________________*/
function sololetra(e) {
    tecla = (document.all) ? e.keyCode : e.which;
    if (tecla==8) return true;
    patron =/[A-Za-z\s]/;//patron Solo acepta letras
    te = String.fromCharCode(tecla);
    return patron.test(te);  
 }
/*____________________________________________________________________*/
function solonumero(e) {
    tecla = (document.all) ? e.keyCode : e.which;
    if (tecla==8) return true;
    patron = /\d/; //patron Solo acepta numeros
    te = String.fromCharCode(tecla);
    return patron.test(te);
} 
/*____________________________________________________________________*/
function vacios(form)
{
  for(i=0;i<document.formulario.length;i++)
    if (document.formulario.elements[i].value=="")
    {
      alert("Debe completar el formulario")
      return false
    }
 return true   
}
/*____________________________________________________________________*/

