from googlesearch import search
import re

def query(res):
    google_table = search(res, tld="co.in", num=40, stop=10, pause=2)
    google_dict = {}
    for i in google_table:
        domain_name = re.search(r"(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]",i)
        if domain_name.group(0) not in google_dict:
            google_dict[domain_name.group(0)] = i
    google_table = [link for link in google_dict.values()]
    return google_table
    