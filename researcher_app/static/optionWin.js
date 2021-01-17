function showWindow(evt){
    let el = document.getElementById("opt_win");

    if(el.style.display.length == 0 || el.style.display.localeCompare("none") == 0) {
        let position = evt.target.getBoundingClientRect();
        el.style.display = "block";
        el.style.top = position["top"]+30;
        el.style.left = position["left"];
    }
    else {
        el.style.display = "none";
    }
}

function closeWindow(evt){
    let target = evt.target;

    if(!document.getElementById("opt_win").parentNode.contains(target)){
        if(target.id) {
            if(target.id.localeCompare("option_btn")!=0){
                hideOptWin();
            }
        }
        else {
            hideOptWin();
        }
    }
}

function hideOptWin(){
    let el = document.getElementById("opt_win");

    if(el) {
        el.style.display = "none";
    }
}

document.getElementById("option_btn").addEventListener("click", showWindow);
document.addEventListener("click", closeWindow);