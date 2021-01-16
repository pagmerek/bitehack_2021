import wikipedia

def query(request):
    
    # problem with disambiguity - try catch? no idea how to address that yet
    try:
        # get only 2 first sentences of the summary to be most concise.
        page = wikipedia.page(request) 

    except wikipedia.DisambiguationError:
        print("DisambiguationError: page resolved to Disambiguation page.")
        return ""

    except wikipedia.PageError:
        print("PageError: Wikipedia didn't match a query.")
        return ""

    except wikipedia.RedirectError:
        print("RedirectError: Page title unexpectedly resolved to a redirect.")
        return ""

    except wikipedia.HTTPTimeoutError:
        print("HTTPTimeoutError: a request to the Mediawiki servers timed out")

    page_summary = wikipedia.summary(request, sentences = 2)
    image = page.images[0]

    # it's possible to load images with page.images, page.images[0] for the first image.

    # uncomment if page title may be useful
    # return page.title, summary
    return page.title, page_summary, image


