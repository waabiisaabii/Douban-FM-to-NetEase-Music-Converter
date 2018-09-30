# Douban-FM-to-NetEase-Music-Converter
## Workflow

`//TODO`

Douban
+ login to douban.fm
+ get song list by user (each song is uniquely identified using `sid`
+ get metadata for all songs
+ save as `.json`

NetEase

+ login
+ create new playlist (__tricky__)
```
for each song from douban:
  douban@sid -> netease@trackId
  add netease@trackId to playlist
```
