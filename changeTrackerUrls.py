from datetime import datetime
import qbittorrentapi
import config

badURL = ''
goodURL = ''

conn_info = dict(
    host="127.0.0.1",
    port=8080,
    username=config.QBITTORRENT_USERNAME,
    password=config.QBITTORRENT_PASSWORD,
)
qbt_client = qbittorrentapi.Client(**conn_info)
qbt_client.auth_log_in()

for torrent in qbt_client.torrents_info():
    for tracker in torrent.trackers:
        if badURL in tracker.url:
            torrent.remove_trackers(urls=[tracker.url])
            torrent.add_trackers(urls=goodURL)            
            print(f"fixed {torrent.name}")