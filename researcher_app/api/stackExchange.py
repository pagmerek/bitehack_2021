import stackexchange as ste

def query(res):
    so = ste.Site(ste.StackOverflow)
    stack_table = []
    for j, i in enumerate(so.search(intitle=res,sort='votes')):
        if j > 10: break
        if(i.owner):
            stack_table.append([i.owner.profile_image, i.owner.display_name, i.score, i.title, i.link])
    return stack_table
