function guardardatos(){
    localStorage.nombre = document.getElementById("nombre").value;
    localStorage.movil = document.getElementById("movil").value;
}

function recuperardatos(){
    if ((localStore.nombre != undefined)&&(localStore.movil != undefined)) {
        document.getElementById("datos").innerHTML = "Nombre: " + localStorage.nombre + "<br> Num. Celular: " + localStorage.movil; 
    } else {
        alert("No has ingresado datos en la agenda")
    }
}

