import yt_dlp

def download_video(url, save_path="."):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f"{save_path}/%(title)s.%(ext)s",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

video_url = input("Enter YouTube video URL: ")
download_video(video_url)
