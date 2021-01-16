from googlesearch import search

def query(res):
    google_table = [z for z in search(res, tld="co.in", num=10, stop=10, pause=2)]
    return google_table
    

