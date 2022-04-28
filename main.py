import youtube_dl

ydl_opts = {
     "format": "best",
     # 'format': 'bestaudio/best',
     # 'postprocessors': [{
     #         'key': 'FFmpegExtractAudio',
     #         'preferredcodec': 'mp3',
     #         'preferredquality': '192',
     #     }],
}
list_url = ['']
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
     for url in list_url:
          ydl.download([url])
