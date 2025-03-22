# utils.py

import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from textblob import TextBlob
from keybert import KeyBERT
from gtts import gTTS
import os
from transformers import pipeline

# Initialize models
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
kw_model = KeyBERT()
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")


def get_news_articles(company_name, max_articles=10):
    query = company_name.replace(" ", "+")
    url = f"https://www.bing.com/news/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    articles = []
    count = 0

    for item in soup.find_all("a", href=True):
        title = item.get_text()
        link = item["href"]
        if link.startswith("http") and len(title) > 30:
            try:
                article_res = requests.get(link, timeout=5)
                article_soup = BeautifulSoup(article_res.text, "html.parser")
                paragraphs = article_soup.find_all("p")
                content = " ".join(p.get_text() for p in paragraphs)
                if len(content) > 200:
                    articles.append({
                        "title": title,
                        "url": link,
                        "content": content
                    })
                    count += 1
                if count >= max_articles:
                    break
            except:
                continue
    return articles


def summarize_text(text):
    summary = summarizer(text[:1024], max_length=120, min_length=30, do_sample=False)[0]['summary_text']
    return summary


def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"


def extract_topics(text, n=5):
    keywords = kw_model.extract_keywords(text, top_n=n)
    return [kw[0] for kw in keywords]


def generate_hindi_tts(text, filename="summary_hi.mp3"):
    # Translate the English summary to Hindi
    hindi_translation = translator(text, max_length=512)[0]["translation_text"]
    
    # Generate Hindi TTS
    tts = gTTS(text=hindi_translation, lang='hi')
    tts.save(filename)
    return filename

if __name__ == "__main__":
    company = "Tesla"

    print("🔍 Fetching news articles...")
    articles = get_news_articles(company)

    for i, article in enumerate(articles):
        print(f"\n📰 Article {i+1}: {article['title']}")
        summary = summarize_text(article["content"])
        sentiment = get_sentiment(article["content"])
        topics = extract_topics(article["content"])

        print("📄 Summary:", summary)
        print("😊 Sentiment:", sentiment)
        print("🔑 Topics:", topics)

    print("\n🎤 Generating Hindi TTS for summary of Article 1...")
    hindi_text = summarize_text(articles[0]["content"])
    generate_hindi_tts(hindi_text)
    print("✅ Hindi TTS saved as 'summary_hi.mp3'")
