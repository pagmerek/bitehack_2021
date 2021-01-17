answersColors = ["#CC6666", "#CEAA78", "#FF9966", "#D99A6C", "#99CC99"]


function setColor(divAnswer) {
    divAnswer.style.backgroundColor = answersColors[Math.floor(Math.random() * answersColors.length)];
}

const answers = document.getElementsByClassName("answer");

if(answers) {
    for (let i = 0; i < answers.length; i++) {
        setColor(answers[i]);
    }
}