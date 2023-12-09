window.addEventListener("load",() =>{
        
    document.querySelector(".loader").classList.add("loader--hidden");

    document.querySelector(".loader").addEventListener("transitioned",() =>{
    document.body.removeChild(document.querySelector(".loader"));    
    })
});

function menuopen() {
    document.getElementById("menu").style.height = "500px";
}

function menuclose() {
    document.getElementById("menu").style.height = "0";
}



function openMenu() {
    document.getElementById("sidebar").style.width = "250px";
}

function closeMenu() {
    document.getElementById("sidebar").style.width = "0";
}


let allow = document.getElementById("allow")

let cookies = document.getElementById("cookies")


allow.addEventListener("click",function(){
    cookies.style.display="none"
});

