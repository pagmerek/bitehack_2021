from django.shortcuts import render
from researcher_app.forms import SearchForm
from researcher_app.api.wiki import query as wiki_query
from researcher_app.api.wolfram import query as wolfram_query
from researcher_app.api.google import query as google_query
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            text = form['search_text'].value()
            google_answer = google_query(text)
            wolfram_answer = wolfram_query(text)
            wiki_answer = wiki_query(text)
            answers = [google_answer, wolfram_answer, wiki_answer]
            return render(request, 'index.html', {'form':form,'answers': answers, 'success':True})
    else:
        form = SearchForm()

    return render(request, 'index.html', {'form': form})

