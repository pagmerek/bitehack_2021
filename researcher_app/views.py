from django.shortcuts import render
from researcher_app.forms import SearchForm
from researcher_app.api.wiki import query as wiki_query
from researcher_app.api.wolfram import query as wolfram_query
from researcher_app.api.google import query as google_query
from researcher_app.api.stackExchange import query as stack_query
# Create your views here.
def index(request):
    if request.method == 'POST':
        apis = request.POST.getlist("api")
        form = SearchForm(request.POST)
        if form.is_valid():
            print(apis)
            text = form['search_text'].value()
            google_answer, wolfram_answer, wolfram_image, wiki_answer, wiki_image,stack_answers = "","",[],"","",[]
            if 'google' in apis:
                google_answer = google_query(text)
            if 'wikipedia' in apis:
                wiki_answer,wiki_image = wiki_query(text)
            if 'wolfram' in apis:
                wolfram_answer,wolfram_image = wolfram_query(text)
            if 'stack' in apis:
                stack_answers = stack_query(text)
            answers = []
            print(wiki_answer,wolfram_answer)
            if wiki_answer != "":
                answers.append(('Wikipedia', wiki_answer ))
            if wolfram_answer != "":
                answers.append(('Wolfram', wolfram_answer))
           
            links = google_answer
            images = [wiki_image]
            images.extend(wolfram_image)
            if images[0] == '': images.remove('')
            return render(request, 'index.html', {'form':form,'answers': answers, 'images':images,'links':links,
                                                    'stack_answers':stack_answers, 'success':True})
    else:
        form = SearchForm()

    return render(request, 'index.html', {'form': form})

