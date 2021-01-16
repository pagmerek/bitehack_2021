from django.shortcuts import render
from researcher_app.forms import SearchForm
from researcher_app.api.wiki import query
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            text = form['search_text'].value()
            print(query(text))
            return render(request, 'index.html', {'form':form, 'success':True})
    else:
        form = SearchForm()

    return render(request, 'index.html', {'form': form})

