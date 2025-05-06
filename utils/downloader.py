from pytube import YouTube
import os

def download_audio(youtube_url, output_path="temp/"):
    """Download audio dari YouTube sebagai MP4"""
    os.makedirs(output_path, exist_ok=True)
    yt = YouTube(youtube_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    filename = audio_stream.download(output_path=output_path)
    return filename
