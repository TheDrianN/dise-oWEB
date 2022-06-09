const mensajes= ['¡Ganaste!','¡Perdiste!','¡Empate!']
const imagenes = [['img/piedra.png','Símbolo de piedra'], ['img/papel.png', 'Símbolo de papel'], ['img/tijera.png', 'Símbolo de tijera']]

let puntosJ=0;
let puntosM=0;
let ganador
let winner

const piedra = 0
const papel = 1
const tijera = 2
const Respuesta = [
        2, 0, 1,
        1, 2, 0,
        0, 1, 2
    ];

const puntosjugador= document.getElementById('resultadoj')
puntosjugador.textContent=puntosJ;

const puntosmaquina=document.getElementById('resultadom')
puntosmaquina.textContent=puntosM;
const resultado = document.getElementById('resultadoJuego')

const eligiopapel = document.getElementById('papel')
eligiopapel.addEventListener('click',()=>{
    decision(papel)
})
const eligiopiedra = document.getElementById('piedra')
eligiopiedra.addEventListener('click',()=>{
    decision(piedra)
})
const eligiotijera= document.getElementById('tijera')
eligiotijera.addEventListener('click',()=>{
    decision(tijera)
})
function decision(jugador){
    let maquina = Math.round(Math.random() * 2);
    winner = Respuesta[jugador + maquina *3];
    let resultadoFinal = [
        mensajes[winner], imagenes[jugador][0],imagenes[jugador][1],imagenes[maquina][0]
        ,imagenes[maquina][1]
    ];
    actualizarpuntos(resultadoFinal);
}

function  actualizarpuntos(resultadoFinal){
    switch(winner){
        case 0:
            puntosJ++
            puntosjugador.textContent=puntosJ
            break;
        case 1:
                puntosM++
                puntosmaquina.textContent=puntosM
                break;

    }
    playerChoiceImg.src = resultadoFinal[1]
playerChoiceImg.alt = resultadoFinal[2]
machineChoiceImg.src = resultadoFinal[3]
machineChoiceImg.alt = resultadoFinal[4]
resultado.textContent = resultadoFinal[0]
}
const playerChoiceImg = document.getElementById('ejugador')
const machineChoiceImg = document.getElementById('emaquina')

