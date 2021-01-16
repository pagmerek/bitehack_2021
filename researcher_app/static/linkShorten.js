function shortenURLs(links) {
    links = links.children;
    for (let i = 0; i < links.length; i++) {
        let url = links[i].textContent;
        let startInd = url.indexOf("//") + 2;
        let endInd = url.indexOf("/", 10);
        links[i].textContent = url.substring(startInd, endInd);
    }
}

const answersLinks = document.getElementsByClassName("answer_links");

if(answersLinks) {
    for (let i = 0; i < answersLinks.length; i++) {
        shortenURLs(answersLinks[i]);
    }
}