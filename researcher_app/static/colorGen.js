answersColors = ["#FBF55A", "#A1FB5A", "#B45AFB", "#5ACBFB", "#FBC45A", "#5A60FB", "#FB5AD7", "#FB5A5A"]

function setColor(divAnswer) {
    divAnswer.style.backgroundColor = answersColors[Math.floor(Math.random() * answersColors.length)];
}

const answers = document.getElementsByClassName("answer");

if(answers) {
    for (let i = 0; i < answers.length; i++) {
        setColor(answers[i]);
    }
}