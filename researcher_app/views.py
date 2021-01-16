from django.shortcuts import render
from researcher_app.forms import SearchForm, SelectForm
from researcher_app.api.wiki import query as wiki_query
from researcher_app.api.wolfram import query as wolfram_query
from researcher_app.api.google import query as google_query
from researcher_app.api.stackExchange import query as stack_query
# Create your views here.
def index(request):
    if request.method == 'POST':
        select_form = SelectForm()
        form = SearchForm(request.POST)
        if form.is_valid():
            text = form['search_text'].value()
            google_answer = google_query(text) if select_form.google else []
            wolfram_answer, wolfram_image = wolfram_query(text) if select_form.wolfram else "", []
            wiki_title, wiki_summary, wiki_image = wiki_query(text) if select_form.wikipedia else "","",""
            answers = [('Wikipedia',wiki_title + ' ' + wiki_summary),('Wolfram',wolfram_answer)]
            stack_answers = stack_query(text)
            links = google_answer
            images = [wiki_image]
            images.extend(wolfram_image)
            return render(request, 'index.html', {'form':form,'select_form':select_form, 'answers': answers, 'images':images,'links':links,
                                                    'stack_answers':stack_answers, 'success':True})
    else:
        form = SearchForm()
        select_form = SelectForm()

    return render(request, 'index.html', {'form': form,'select_form':select_form})

