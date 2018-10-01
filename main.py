import sys
import pickle

from douban_util.get_songs import get_song_ids, get_song_detailed_json
from douban_util.login import get_douban_dbcl2

username = sys.argv[1]
password = sys.argv[2]

cookie_dbcl2 = get_douban_dbcl2(username=username,
                                password=password)
song_ids = get_song_ids(cookie_dbcl2=cookie_dbcl2)





# song_ids_partitioned = get_list_partitioned(song_ids, 30)
song_list_detailed_json = get_song_detailed_json(song_ids=song_ids,
                                            cookie_dbcl2=cookie_dbcl2)

with open('song_list_detailed.json', 'w') as f:
    pickle.dump(song_list_detailed_json, f)
