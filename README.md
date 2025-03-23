# akaike-news-app
# akaike-news-app
# 📰 Company News Summarizer with Hindi TTS
This project is a complete news analysis tool built using Python and Gradio. You just enter a company name, and the app does the rest — it fetches the latest news articles, summarizes them, analyzes the sentiment, extracts key topics, and even reads out a summary in Hindi!
I built this as part of the Akaike Internship Assignment to demonstrate my skills in applied machine learning, NLP, and building real-world AI products.
---
## 🚀 What the App Can Do
- 🔍 **Fetches News:** Pulls the latest 10 articles related to a company
- 📄 **Summarizes:** Uses a Transformer model to generate concise summaries
- 😊 **Analyzes Sentiment:** Tags each article as Positive, Neutral, or Negative
- 🔑 **Extracts Topics:** Pulls out key topics using KeyBERT
- 🎙️ **Generates Hindi Audio:** Translates the first summary to Hindi and uses TTS to create audio
- 📥 **Download Options:** You can download both the summary text and the audio
---
## 🧠 Technologies Used
- `transformers` – for summarization and translation
- `gTTS` – for text-to-speech in Hindi
- `textblob` – for sentiment analysis
- `keybert` – for keyword/topic extraction
- `beautifulsoup4` – for scraping news
- `gradio` – for the user interface
- Python 3.11 + libraries like `torch`, `nltk`, `sentencepiece`, etc.
---
## 🛠 How to Run the App Locally
If you want to try this on your machine:
```bash
git clone https://github.com/vaankush/akaike-news-app
cd akaike-news-app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
---
<details>
<summary><strong>
  
📦 Project Structure
  
  (click to expand)</strong></summary>

```
akaike-news-app/
├── app.py                  # Main Gradio interface
├── utils.py                # Core functions: summarization, sentiment, keywords, TTS
├── requirements.txt        # Python dependencies
├── README.md               # This file!
├── summary_hi.mp3          # Hindi audio summary (auto-generated)
├── summary_XXXX.txt        # Text summary download (auto-generated)
└── venv/                   # Virtual environment (excluded from GitHub)
```
</details>

---

## 🧪 Example Output
Let’s say you search for **Tesla**:
- Total Articles: 10  
- Positive: 6  
- Neutral: 3  
- Negative: 1  
- 🔥 Most Frequent Topics: tesla, ev, india, elon musk, partnership  
- 🎧 Plays Hindi summary of the first article  
- 📄 Lets you download everything!
---
## 🌐 Live Demo
👉 https://huggingface.co/spaces/vaankush/akaike-news-app
---


## 🙏 A Note of Thanks
Thanks to Akaike Technologies for this creative challenge — it was a great opportunity to build something practical from scratch. Also grateful to Hugging Face and the open-source ML community for making these tools accessible.
---

## 👋 About Me
Hi! I’m Subhashree Prabakaran, an Artificial Intelligence & Data Science student. I enjoy building real-world AI tools and exploring how technology can solve meaningful problems.  
📧 vaankuil3@gmail.com  
🔗 https://www.linkedin.com/in/subhashree-meenaakshi/
