from youtubesearchpython import VideosSearch

def query(res):
    video_table = []
    videosSearch = VideosSearch(res, limit = 3)
    result = videosSearch.result()['result']
    for i in result:
        video_table.append([i['title'], i['thumbnails'][0]['url'], i['link']])
    return video_table

