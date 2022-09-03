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

async function unblur() {

 	
    const teasers = await fetch("https://api.gotinder.com/v2/fast-match/teasers", { "headers": { "X-Auth-Token": localStorage.getItem('TinderWeb/APIToken') }}).then(res => res.json()).then(res => res.data.results);
  
       
    const teaserEls = document.querySelectorAll('.Expand.enterAnimationContainer > div:nth-child(1)');
  
       
   
  
       
    for (let i = 0; i < teaserEls.length; ++i) {
  
       
      const teaser = teasers[i];
  
       
      const teaserEl = teaserEls[i];
  
       
     
  
       
      const teaserImage = teaser.user.photos[0].url;
  
       
     
  
       
      teaserEl.style.backgroundImage = `url(${teaserImage})`;
  
       
    }
  
       
  }
  
       
   
  
       
  setInterval(() => {
  
       
      if (['/app/likes-you', '/app/gold-home'].includes(location.pathname)) {
  
       
        unblur();
  
       
      }
  
       
  }, 5000);