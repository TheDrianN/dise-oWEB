function zoom(){
    var thumb = document.getElementById('thumb');
    if(thumb.getAttribute("width")=="200"){ 
 
     thumb.setAttribute("width", "500");
     thumb.style.transition = "400ms all ease";
 
    }else{
     thumb.setAttribute("width", "200");
    }
   } 
   
   