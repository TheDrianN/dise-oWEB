

const maquina3= document.getElementById('texto3');

const maquinaEscribir1 = (text='',tiempo=200,etiqueta='')=>{
    let arrayCaracteres = text.split('')
    etiqueta.innerHTML=''
    let cont=0
    let escribir = setInterval(function(){
        etiqueta.innerHTML += arrayCaracteres[cont]
        cont++
        if(cont === arrayCaracteres.length){
            clearInterval(escribir)
        }
    },tiempo)
}

maquinaEscribir1("Preparate para la aventura",100,maquina3);

function toggle(elemento) {
    (elemento.value == "Cerrar")
    document.getElementById("myModal").style.display = "none";
}