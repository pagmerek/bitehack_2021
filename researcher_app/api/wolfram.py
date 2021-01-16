import wolframalpha

app_id = 'W3L5WX-P6EAVKL8XV'
client = wolframalpha.Client(app_id)

def query(req):
    res = client.query(req)

    def wolframCheckRes(res):
        status = res['@success'] and not(res['@error'])
        return status

    if wolframCheckRes(res):
        return next(res.results).text
    else:
        return ""


