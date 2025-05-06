import streamlit as st
from utils.downloader import download_audio
from utils.transcriber import transcribe_audio
from utils.summarizer import summarize_text
import os

# Konfigurasi UI
st.title("YouTube Downloader + AI Transkrip & Ringkasan")
youtube_url = st.text_input("Masukkan URL YouTube:")

if st.button("Proses"):
    if youtube_url:
        with st.spinner("Mendownload audio..."):
            audio_path = download_audio(youtube_url)
        
        with st.spinner("Mentranskrip audio..."):
            transcript = transcribe_audio(audio_path)
            st.subheader("Transkrip Lengkap:")
            st.text_area("", transcript, height=200)
        
        with st.spinner("Membuat ringkasan..."):
            summary = summarize_text(transcript)
            st.subheader("Ringkasan:")
            st.write(summary)
        
        # Bersihkan file sementara
        os.remove(audio_path)
    else:
        st.error("Harap masukkan URL YouTube!")
