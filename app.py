# app.py

from collections import Counter
import uuid
import gradio as gr
from utils import (
    get_news_articles,
    summarize_text,
    get_sentiment,
    extract_topics,
    generate_hindi_tts
)

def analyze_company_news(company_name):
    articles = get_news_articles(company_name)
    results = []

    sentiment_count = {'Positive': 0, 'Negative': 0, 'Neutral': 0}
    all_topics = []

    for article in articles:
        summary = summarize_text(article["content"])
        sentiment = get_sentiment(article["content"])
        topics = extract_topics(article["content"])

        sentiment_count[sentiment] += 1
        all_topics.extend(topics)

        results.append({
            "title": article["title"],
            "summary": summary,
            "sentiment": sentiment,
            "topics": topics
        })

    keyword_freq = Counter(all_topics).most_common(5)

    # Generate Hindi TTS from the first article's summary
    if results:
        tts_path = generate_hindi_tts(results[0]["summary"])
    else:
        tts_path = ""

    return results, tts_path, sentiment_count, keyword_freq


def save_summary_to_txt(summary_text):
    filename = f"summary_{uuid.uuid4().hex[:8]}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(summary_text)
    return filename


def format_output(results, audio_path, sentiment_count, keyword_freq):
    output_text = ""
    for i, res in enumerate(results):
        output_text += f"📰 **Article {i+1}: {res['title']}**\n"
        output_text += f"- 📄 Summary: {res['summary']}\n"
        output_text += f"- 😊 Sentiment: {res['sentiment']}\n"
        output_text += f"- 🔑 Topics: {', '.join(res['topics'])}\n\n"

    # Add summary insights
    output_text += "---\n"
    output_text += "## 📊 Summary Insights\n"
    output_text += f"- Total Articles: {len(results)}\n"
    output_text += f"- 😊 Positive: {sentiment_count['Positive']}\n"
    output_text += f"- 😐 Neutral: {sentiment_count['Neutral']}\n"
    output_text += f"- ☹️ Negative: {sentiment_count['Negative']}\n\n"
    output_text += "**🔥 Most Frequent Topics:**\n"
    for topic, freq in keyword_freq:
        output_text += f"- {topic} ({freq} times)\n"

    summary_file = save_summary_to_txt(output_text)
    return output_text, audio_path, audio_path, summary_file


def run_app(company_name):
    results, audio_path, sentiment_count, keyword_freq = analyze_company_news(company_name)
    return format_output(results, audio_path, sentiment_count, keyword_freq)


iface = gr.Interface(
    fn=run_app,
    inputs=gr.Textbox(label="Enter a Company Name", placeholder="e.g. Tesla"),
    outputs=[
        gr.Markdown(label="News Summary & Sentiment"),
        gr.Audio(label="Hindi Audio Summary"),
        gr.File(label="Download Hindi Audio"),
        gr.File(label="Download Summary (.txt)")
    ],
    title="📰 Company News Summarizer with Sentiment & Hindi TTS",
    description="Enter a company name to get summarized news, sentiment analysis, and an audio summary in Hindi."
)

if __name__ == "__main__":
    iface.launch()

