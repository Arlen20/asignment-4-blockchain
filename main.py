import streamlit as st
from news_api import get_news
from price_api import get_binance_price
from market_api import get_coin_info
from ollama_chat import ask_ollama

# Page Configuration
st.set_page_config(page_title="🧠 AI Crypto Assistant", layout="centered")

# Header
st.title("💡 AI Crypto Assistant")
st.caption("🔗 Powered by Binance, CoinGecko, CryptoPanic & Ollama")

# Intro Section
st.markdown(
    """
### 🌟 Features:
- 📊 Real-time **market insights**
- 🗞️ Curated **crypto news**
- 💬 Smart **AI-powered answers**
"""
)

# User Input
st.markdown("### 🧠 Ask about any cryptocurrency")
user_query = st.text_input("Example: What is Ethereum? or Show me Bitcoin price")

if st.button("🚀 Get Info") and user_query:
    coin = user_query.split()[-1].lower()

    with st.spinner("⏳ Gathering live data..."):
        news = get_news(coin)
        price = get_binance_price(coin)
        coin_info = get_coin_info(coin)

        if isinstance(coin_info, dict):
            coin_name = coin_info['name']
            coin_symbol = coin_info['symbol']
            coin_image = coin_info.get("image", "")
            facts = f"""
**Coin**: {coin_name} ({coin_symbol})  
**Rank**: #{coin_info['rank']}  
**Market Cap**: ${coin_info['market_cap']:,.2f}  
**Price (CoinGecko)**: ${coin_info['price']:,.2f}  
**Price (Binance)**: ${price}
            """
        else:
            facts = coin_info
            coin_name = None
            coin_symbol = None
            coin_image = None

        news_text = "\n".join([f"{i+1}. {n}" for i, n in enumerate(news)])
        ai_prompt = f"""
A user asked: "{user_query}"

Here is the latest live market data:

{facts}

Latest news headlines:
{news_text}

Please summarize the market data and the news above, and give the user a clear, helpful answer.
        """
        ai_answer = ask_ollama(ai_prompt)

    # Display Results
    if coin_name:
        st.markdown(f"## 🔍 {coin_name} ({coin_symbol})")
        if coin_image:
            st.image(coin_image, width=64)

    st.markdown("### 🤖 Assistant Response")
    st.success(ai_answer)

    # Market Info
    with st.expander("📉 Market Overview"):
        if isinstance(coin_info, dict):
            col1, col2, col3 = st.columns(3)
            col1.metric("💵 Price", f"${coin_info['price']:,.2f}")
            col2.metric("💼 Market Cap", f"${coin_info['market_cap']:,.0f}")
            col3.metric("🏅 Rank", f"#{coin_info['rank']}")
            st.markdown("#### 📋 Full Data")
            st.code(facts)
        else:
            st.error(facts)

    # News Info
    with st.expander("📰 Latest News Headlines"):
        for item in news:
            st.write("🔸 " + item)
