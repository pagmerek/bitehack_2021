import wolframalpha

app_id = 'W3L5WX-P6EAVKL8XV'
client = wolframalpha.Client(app_id)

def wolframGetRes(query):
    res = client.query(query)

    if wolframCheckRes(res):
        return next(res.results).text
    else:
        return ""

def wolframCheckRes(res):
    status = res['@success'] and not(res['@error'])
    return status
