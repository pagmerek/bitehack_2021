import wolframalpha

def query(request):

    app_id = 'W3L5WX-P6EAVKL8XV'
    client = wolframalpha.Client(app_id)

    res = client.query(request)

    try: 
        return next(res.results).text
    
    # usually this is the standard library python error we get when wolfram can't find anything
    except StopIteration:
        return ""

