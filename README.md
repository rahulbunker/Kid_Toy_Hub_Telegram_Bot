# 🤖 Kid Toy Hub Telegram Bot

An AI-powered customer support Telegram bot for **Kid Toy Hub** — a RC toys and kids toys store serving both **India 🇮🇳** and **USA 🇺🇸**. The bot is built with Python, powered by **Groq's LLaMA 3.3 70B** model, and deployed via `python-telegram-bot`.

---

## 📌 Features

- 🚗 **Product Recommendations** — Helps customers choose the right RC cars, bikes, helicopters, and educational toys based on age
- 💰 **Pricing Info** — Provides pricing in both INR (India) and USD (USA)
- 🚚 **Shipping Details** — Answers queries about delivery timelines and charges for both countries
- ↩️ **Return Policy** — Informs customers about the 7-day return window and refund process
- 🎉 **Offers & Discounts** — Shares active discount codes and festive sale info
- 🌐 **Bilingual Support** — Responds in **Hinglish** if the user writes in Hindi/Hinglish, English otherwise
- 💬 **AI-Powered Conversations** — Uses Groq's LLaMA 3.3 70B model for natural, context-aware replies
- ⌨️ **Typing Indicator** — Shows a "typing..." status while generating a response for a better UX

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.11+ |
| Telegram Framework | `python-telegram-bot` v21.6 |
| AI Model | Groq — `llama-3.3-70b-versatile` |
| Environment Variables | `python-dotenv` |
| HTTP Client | `httpx` |
| Deployment (optional) | `gunicorn` |

---

## 📁 Project Structure

```
Kid_Toy_Hub_Telegram_Bot/
│
├── bot.py              # Main bot logic — handlers, AI integration
├── requirements.txt    # Python dependencies
├── runtime.txt         # Python version for deployment
├── .gitignore          # Ignored files (env, cache, etc.)
└── README.md           # Project documentation
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/rahulbunker/Kid_Toy_Hub_Telegram_Bot.git
cd Kid_Toy_Hub_Telegram_Bot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Linux / Mac
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```env
TELEGRAM_TOKEN=your_telegram_bot_token_here
GROQ_API_KEY=your_groq_api_key_here
```

> **How to get these keys:**
> - **Telegram Token** — Talk to [@BotFather](https://t.me/BotFather) on Telegram → create a new bot → copy the token
> - **Groq API Key** — Sign up at [console.groq.com](https://console.groq.com) → go to API Keys → create a new key

### 5. Run the Bot

```bash
python bot.py
```

You should see:
```
🤖 Kid Toy Hub Bot chal raha hai... Ctrl+C se band karo
```

---

## 💬 Bot Commands

| Command | Description |
|---|---|
| `/start` | Welcome message + introduction |
| `/help` | Shows what questions you can ask the bot |
| Any text message | AI-powered response via Groq LLaMA |

---

## 🧠 How It Works

1. User sends a message on Telegram
2. `python-telegram-bot` receives the message and triggers the `handle_message` handler
3. The message is passed to the **Groq API** along with a detailed **system prompt** that defines the bot's persona, product knowledge, pricing, shipping rules, and tone
4. Groq returns an AI-generated response using **LLaMA 3.3 70B**
5. The response is sent back to the user in Telegram
6. If an error occurs, a friendly fallback message is shown with the support email

---

## 📋 System Prompt Coverage

The bot is trained (via system prompt) to handle:

- 🚗 RC cars, trucks, bikes, helicopters — product info and age recommendations
- 💰 Pricing in ₹ (India) and $ (USA)
- 🚚 Shipping timelines and free shipping thresholds
- ↩️ 7-day return policy and refund process
- 🎉 Discount codes and festive offers
- 📞 Customer support contact details
- 🗣️ Hinglish replies when the user writes in Hindi

---

## 🚀 Deployment

This bot can be deployed on any Python-compatible hosting platform.

### Option 1 — Railway (Free Tier)

1. Push your code to GitHub
2. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Add environment variables (`TELEGRAM_TOKEN`, `GROQ_API_KEY`) in the Variables tab
4. Railway will auto-detect Python and run the bot

### Option 2 — Render (Free Tier)

1. Go to [render.com](https://render.com) → New Web Service
2. Connect your GitHub repo
3. Set **Start Command** to: `python bot.py`
4. Add environment variables in the Environment section

### Option 3 — Local (Always Running)

Use `screen` or `tmux` on a Linux server to keep the bot running:

```bash
screen -S kidtoybot
python bot.py
# Ctrl+A then D to detach
```

---

## 📦 Dependencies

```
python-telegram-bot==21.6
groq==0.9.0
python-dotenv==1.0.0
httpx==0.27.2
gunicorn==23.0.0
```

---

## 🔒 Security Notes

- Never commit your `.env` file — it's already in `.gitignore`
- Keep your `TELEGRAM_TOKEN` and `GROQ_API_KEY` private at all times
- If your token is accidentally exposed, immediately revoke it via BotFather / Groq Console

---

## 📺 About Kid Toy Hub

**Kid Toy Hub** is a YouTube & Facebook channel dedicated to RC toy unboxing and kids toy play videos, targeting audiences in both India and the USA. This bot serves as an automated customer support assistant for the brand.

- 📺 YouTube: [Kid Toy Hub](https://youtube.com/@KidToyHub)
- 📘 Facebook: [Kid Toy Hub](https://facebook.com/KidToyHub)
- 📧 Support: support@kidtoyhub.com

---

## 👨‍💻 Author

**Rahul** — [@rahulbunker](https://github.com/rahulbunker)

M.Sc Data Science Student | AI/ML Engineer | IIIT Lucknow

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
