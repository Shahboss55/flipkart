// function myfunc() {
//     var name = document.getElementById("rr").innerHTML;
//     if (name == "rahul"){
//         document.getElementById("rr").innerHTML = "shah";}
//     else {document.getElementById("rr").innerHTML = "rahul";}
// }

// var icon = document.querySelector("#icon");
// var ul = document.querySelector("ul");

// icon.addEventListener("click",()=>{
//     ul.classList.toggle("data");
//     console.log(ul);
// })
function shah() {
    let ul = document.querySelector("ul");
    ul.classList.toggle("dara");

    if(ul.className == "dara"){
        document.getElementById("bar").className = "fa-solid fa-xmark";
    }
    else{
        document.getElementById("bar").className = "fa-solid fa-bars";
    }
}