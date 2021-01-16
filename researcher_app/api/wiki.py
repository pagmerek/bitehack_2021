import wikipedia

def query(request):
    
    # problem with disambiguity - try catch? no idea how to address that yet
    try:
        page = wikipedia.page(request)

    except wikipedia.DisambiguationError:
        return ""
    

    # get only 2 first sentences of the summary to be most concise.
    summary = page.summary.split('. ', 2)

    # it's possible to load images with page.images, page.images[0] for the first image.

    # uncomment if page title may be useful
    # return page.title, summary
    return summary


