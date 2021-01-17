import wolframalpha

def query(request):

    app_id = 'W3L5WX-P6EAVKL8XV'
    client = wolframalpha.Client(app_id)

    res = client.query(request)
    try: 
        text_val = next(res.results).text
        images = []
        for i in res:
            if(i.get('@title')):
                if isinstance(i['subpod'],list):
                    if int(i['subpod'][0]['img']['@height']) >= 100 and int(i['subpod'][0]['img']['@width']) <= 300:
                        images.append(i['subpod'][0]['img']['@src'])
                else:
                    if int(i['subpod']['img']['@height']) >= 100 and int(i['subpod']['img']['@width']) <= 300:
                        images.append(i['subpod']['img']['@src'])
        return text_val, images 
    
    # usually this is the standard library python error we get when wolfram can't find anything
    except AttributeError:
        return "",[]
    
    except StopIteration:
        return "",[]

