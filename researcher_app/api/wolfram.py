import wolframalpha

app_id = 'W3L5WX-P6EAVKL8XV'
client = wolframalpha.Client(app_id)

def wolframGetRes(query):
    res = client.query(query)

    print(wolframCheckRes(res))
    print(next(res.results).text)

def wolframCheckRes(res):
    status = res['@success'] and not(res['@error'])
    return status

wolframGetRes("cat")
