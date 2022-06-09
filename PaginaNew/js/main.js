/*Audio */
const audio = document.getElementById("audio");
const playPause = document.getElementById("play");

playPause.addEventListener("click",()=>{
    if(audio.paused || audio.ended){
        playPause.querySelector(".pause-btn").classList.toggle("hide");
        playPause.querySelector(".play-btn").classList.toggle("hide");
        audio.play();
    }else{
        audio.pause();
        playPause.querySelector(".pause-btn").classList.toggle("hide");
        playPause.querySelector(".play-btn").classList.toggle("hide");
    }
});


/*caruosel*/
const fila = document.querySelector('.contenedor-carousel');
const  celulares= document.querySelectorAll('.celular');


const flechaIzquierda =  document.getElementById('flecha-izquierda');
const flechaDerecha =  document.getElementById('flecha-derecha');


flechaDerecha.addEventListener('click', () => {
    fila.scrollLeft += fila.offsetWidth;

    const indicadorActivo =  document.querySelector('.indicadores .activo');
    if(indicadorActivo.nextSibling){
        indicadorActivo.nextSibling.classList.add('activo');
        indicadorActivo.classList.remove('activo');
    }
});

flechaIzquierda.addEventListener('click', () => {
    fila.scrollLeft -= fila.offsetWidth;

    const indicadorActivo =  document.querySelector('.indicadores .activo');
    if(indicadorActivo.previousSibling){
        indicadorActivo.previousSibling.classList.add('activo');
        indicadorActivo.classList.remove('activo');
    }
});


const numeroPaginas = Math.ceil(celulares.length /5);
for(let i=0; i<numeroPaginas;i++){
    const indicador =  document.createElement('button');

    if (i ===0 ) {
        indicador.classList.add('activo');
    }
    document.querySelector('.indicadores').appendChild(indicador);
    indicador.addEventListener('click',(e)=>{
        fila.scrollLeft=i *  fila.offsetWidth;
        
        document.querySelector('.indicadores .activo').classList.remove('activo');
        e.target.classList.add('activo');
    })
}

celulares.forEach((celular) =>{
    celular.addEventListener('mouseenter', (e) =>{
        const elmento= e.currentTarget;
        setTimeout(()=>{
            celulares.forEach(celular => celular.classList.remove('hover'));
            elmento.classList.add('hover');
        },300);
    });
});


fila.addEventListener('mouseleave',()=>{
    celulares.forEach(celular => celular.classList.remove('hover'));
})
/*---Car */

/* carrito */
let allcontainerCart = document.querySelector('.carousel');
let buythings = [];
let priceTotal = document.querySelector('.price-total');
let containerBuyCart= document.querySelector('.card-items');
let amountProduct = document.querySelector('.count-product')
let totalCard = 0;
let countProduct=0;

loadEventListenrs();
function loadEventListenrs(){
    allcontainerCart.addEventListener('click',addProduct);
    containerBuyCart.addEventListener('click',deleteProduct);
}

function addProduct(e){
    e.preventDefault();
    if(e.target.classList.contains('boton-add')){
        
        const selectProduct = e.target.parentElement;
        readTheContent(selectProduct);
    }
   
}

function deleteProduct(e){
    if(e.target.classList.contains('delete-product')){
        const deleteId= e.target.getAttribute('data-id');
        buythings.forEach(value=>{
            if(value.id == deleteId){
                let priceReduce= parseFloat(value.price) * parseFloat(value.amount);
                totalCard = totalCard- priceReduce;
                totalCard = totalCard.toFixed(2);
                countProduct--;
            }
        })
        
        buythings = buythings.filter(product => product.id !== deleteId);
    }
    loadHtml();
}



function readTheContent(product){
    const infoProduct = {
        image: product.querySelector('.item-image').src,
        title: product.querySelector('.title').textContent,
        price: product.querySelector('.precio').textContent,
        id: product.querySelector('button').getAttribute('data-id'),
        amount:1

    }

    totalCard =  parseFloat(totalCard) + parseFloat(infoProduct.price);
    totalCard = totalCard.toFixed(2);

    const exist = buythings.some(product => product.id === infoProduct.id)
    if(exist){
        const pro = buythings.map(product =>{
            if(product.id === infoProduct.id){
                product.amount++;
                return product;
            }else{
                return product
            }
        });
        buythings = [...pro];
    }else{
        buythings=[...buythings,infoProduct]
        countProduct++;
    }
    
    loadHtml();
    console.log(infoProduct);
}

function loadHtml(){
    clearHtml();
    buythings.forEach(product =>{
        const{image,title,price,amount, id}=product;
        const row = document.createElement('div');
        row.classList.add('item'),
        row.innerHTML=`
        <img src="${image}">
        <div class="item-content"> 
        <h5>${title}</h5>
        <h5 class="cart-price">${price}</h5>
        <h6> Cantidad:${amount}</h6>
       </div>
       <span class="delete-product" data-id="${id}">X</span>       
       `;
       containerBuyCart.appendChild(row); 
       
       priceTotal.innerHTML = totalCard;
       amountProduct.innerHTML = countProduct;
    });
   
}

function clearHtml(){
    containerBuyCart.innerHTML='';
    amountProduct.innerHTML="0";
    priceTotal.innerHTML="0";
}
