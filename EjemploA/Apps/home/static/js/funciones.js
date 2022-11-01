$(document).on('ready',Iniciar);

window.onload = function () {
    console.log("DOM Cargado");
}

$(document).ready(function(){
    console.log("DOM LISTO PARA INSTURCCIONES");
 });

 $(document).ready(function(){
    $("button").click(function(){
      $("p").hide();
    });
  });

  $(document).ready(function(){
    $("button").click(function(){
      $("#testblock").hide();
    });
  });

function Iniciar(){
    //alert("Hola Mundo");
    console.log("Hola Mundo");
    $varBoton = $('#btnaceptar');
    $varBoton.on('click',Presionar);
    $varBoton = $('#btnagregar');
    $varBoton.on('click',Agregar);
    $varBoton = $('#btnocultar');
    $varBoton.on('click',Ocultar)
}

function Presionar(){
    alert("Boton presionado");
    console.log("boton presionado");
    $varTitulo = $('#main');
    $varTitulo.html("presionaste el boton de abajo");
}

function Agregar(){
    $varFormulario = $("#Formulario");
    $varFormulario.append('<input type="text" name="D" placeholder="Datos">')
    console.log("Se agrego formulario");
}

function Ocultar(){
    $varFormulario = $("#Formulario");
    $varFormulario.hide();
}