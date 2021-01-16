from django.shortcuts import render
from researcher_app.forms import SearchForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            text = form['search_text'].value()
            print(text)
    else:
        form = SearchForm()

    return render(request, 'index.html', {'form': form})

