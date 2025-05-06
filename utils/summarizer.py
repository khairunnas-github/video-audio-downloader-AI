from transformers import pipeline

def summarize_text(text, max_length=150):
    """Ringkas teks menggunakan Hugging Face's BART"""
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=max_length, min_length=30, do_sample=False)
    return summary[0]["summary_text"]
