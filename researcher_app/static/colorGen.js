answersColors = ["#98979C", "#CEAA78", "#CE8350", "#B8613A"]

function setColor(divAnswer) {
    divAnswer.style.backgroundColor = answersColors[Math.floor(Math.random() * answersColors.length)];
}

const answers = document.getElementsByClassName("answer");

if(answers) {
    for (let i = 0; i < answers.length; i++) {
        setColor(answers[i]);
    }
}