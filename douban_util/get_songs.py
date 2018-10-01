import requests
import json

from douban_util import urls


def get_song_ids(cookie_dbcl2):
    print 'Getting heartlist'

    headers = {'Cookie': 'dbcl2=' + cookie_dbcl2 + ';'}
    req = requests.get(url=urls.url_user_basic,
                       headers=headers)

    print 'HTTP status: ', req.status_code
    if (req.status_code is not 200):
        raise Exception("Unexpected response code")

    song_list = json.loads(req.content)[u'songs']

    return [song[u'update_time'] for song in song_list]

def get_song_detailed_json(song_ids, cookie_dbcl2):
    print 'Getting metadata'

    headers = {'Cookie': 'dbcl2=' + cookie_dbcl2 + ';',
               'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'sids': '|'.join([str(id) for id in song_ids]),
            'kbps': '128',
            'ck': ''}
    req = requests.post(url=urls.url_song_list,
                       headers=headers,
                       data=data)
    song_detailed = json.loads(req.content)
    return json.dumps(req.content, sort_keys=True, indent=4)

def get_list_partitioned(given_list, size):
    for i in xrange(0, len(given_list), size):
        yield given_list[i : i + size]

