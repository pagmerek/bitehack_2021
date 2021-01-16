function showLoader(event) {
    hideOptWin();
    hideAnswers();

    let el = document.getElementById("loader");
    el.style.display = "block";
  }

  
function hideAnswers(){
    let el = document.getElementsByClassName("answers")[0];
    if(el) {
        el.style.display = "none";
    }
}
  
const form = document.getElementsByTagName('form')[0];
form.addEventListener('submit', showLoader);