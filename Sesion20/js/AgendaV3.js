function guardarDato(){
    const nombre =  document.getElementById("nombre").value;
    const movil =  document.getElementById("movil").value;
    const email = document.getElementById("email").value;
    const universidad = document.getElementById("universidad").value;

    const datos = {
        'movil' : movil,
        'email' : email,
        'universidad': universidad,
    };

    localStorage.setItem(nombre,JSON.stringify(datos));
    document.getElementById("nombre").value= "";
    document.getElementById("movil").value = "";
    document.getElementById("email").value = "";
    document.getElementById("universidad").value = "";
    actualizarDatos();
}

function recuperarDatos(){
    var nombre =  prompt("Ingresar Nombre Para Recuperar");
    localStorage.getItem(nombre);
    var datosJson = JSON.parse(localStorage.getItem(nombre));
    document.getElementById("nombre").value=nombre;
    document.getElementById("movil").value=datosJson.movil;
    document.getElementById("email").value=datosJson.email;
    document.getElementById("universidad").value=datosJson.universidad;

}

function eliminarDatos(){
    var nombre = prompt("Ingresar Nombre a Eliminar");
    localStorage.removeItem(nombre);
    actualizarDatos();
}
function eliminarTodo(){
    localStorage.clear();
    actualizarDatos();
}

function actualizarDatos(){
    var registro ="";
    if (localStorage.length == 0) {
        registro+= '<li>Vacío</li>';
        
    } else {
        for(var i = 0; i<=localStorage.length - 1; i++){
            var key = localStorage.key(i);
            var datosJson = JSON.parse(localStorage.getItem(key));
            registro += '<div class="tabla">'+ '<div class="nom">'+key+'</div>'+
             '<div class="nom">'+datosJson.movil+'</div>'+
             '<div class="nom">'+datosJson.email+'</div>'+
             '<div class="nom">'+datosJson.universidad+'</div>'+
             '</div><br>';
        }
        
    }
    document.getElementById('contactos').innerHTML = registro;
}

