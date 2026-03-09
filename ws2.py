import yt_dlp

url = "https://www.youtube.com/watch?v=JmTCXIBa0e4&list=RDJmTCXIBa0e4&start_radio=1&pp=ygUVa2ltIGNoYWV3b24gc3BhZ2hldHRpoAcB"

ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])