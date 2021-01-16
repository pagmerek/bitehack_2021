function showWindow(evt){
    let el = document.getElementById("opt_win");

    if(el.style.display.length == 0 || el.style.display.localeCompare("none")==0) {
        let position = evt.originalTarget.getBoundingClientRect();
        el.style.display = "block";
        el.style.top = position["top"]+30;
        el.style.left = position["left"];
    }
    else {
        el.style.display = "none";
    }
}

document.getElementById("option_btn").addEventListener("click", showWindow);