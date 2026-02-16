# 🧠 AI Crypto Assistant

AI-powered **Streamlit** web app that provides quick crypto-market insights using **live off-chain data** + a local **LLM (Ollama)**.

---

## 🚀 Objective

This assistant can:
- Answer user questions about the crypto market in natural language
- Fetch live data from multiple sources (news, price, market stats)
- Generate short, human-readable summaries using an LLM via **Ollama**

---

## ✨ Features

### ✅ Natural Language Queries
Examples:
- “What’s the latest news about Ethereum?”
- “What’s the current price and market cap of Solana?”
- “Show me today’s market overview”

### ✅ Live Data Aggregation (on every query)
- **News** via RSS/news sources
- **Prices** from **Binance**
- **Market stats & rankings** from **CoinGecko**

### ✅ AI-Powered Summaries (Ollama)
- Summarizes news + price + market metrics
- Produces a clear final answer for the user

---
# 📃 Demo Screenshots
![Screenshot 2025-05-16 172741](https://github.com/user-attachments/assets/305326fc-a500-4c41-adb9-c9fdf7944ee3)
![Screenshot 2025-05-16 172751](https://github.com/user-attachments/assets/5330dd3d-980f-4655-b156-60e3efe17f88)
![Screenshot 2025-05-16 172803](https://github.com/user-attachments/assets/2d7b5b5d-7fe3-412c-b6e5-78e5a2865d85)

## 🛠 Requirements

- Python 3.10+
- Streamlit
- (Optional) Ollama for AI summaries

##Install dependencies:
```
pip install -r requirements.txt
▶️ Run Locally
Start the Streamlit app:
streamlit run main.py

##Open in browser:
http://localhost:8501

##🤖 Ollama Setup (Optional but recommended)
Install Ollama and pull (recommended):

ollama pull llama3
If you use another model, update it in ollama_chat.py (default model=).

##📌 Notes / Limitations
Supported coins may be limited to a predefined list in the code (Binance symbol mapping)

If Ollama is not installed, AI summaries will not work (data fetching can still work depending on your setup)

📄 License
MIT License — see LICENSE.
