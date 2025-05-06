import whisper

def transcribe_audio(audio_path):
    """Konversi audio ke teks menggunakan Whisper"""
    model = whisper.load_model("base")  # Gunakan 'small' atau 'medium' untuk akurasi lebih tinggi
    result = model.transcribe(audio_path)
    return result["text"]
