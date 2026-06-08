import os
import logging
from dotenv import load_dotenv
from groq import Groq
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

# .env se keys load karo
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Groq AI client setup
groq_client = Groq(api_key=GROQ_API_KEY)

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ✅ Kid Toy Hub System Prompt
SYSTEM_PROMPT = """
You are a friendly customer support assistant for "Kid Toy Hub" — a popular RC toys and kids toys store serving both India and USA.

Answer customer questions about:

🚗 PRODUCTS:
- RC cars, RC trucks, RC bikes, RC helicopters
- Outdoor toys, educational toys, battery-operated toys
- Age-appropriate recommendations (3+, 6+, 8+ years)

💰 PRICING:
- RC toys: ₹499 – ₹4999 (India) / $10 – $60 (USA)
- Combo deals and festive discounts available
- Bulk orders: contact us for special pricing

🚚 SHIPPING:
- India: Free shipping above ₹599, delivery in 4-6 business days
- USA: Free shipping above $25, delivery in 7-10 business days
- Express delivery available at extra charge

↩️ RETURN POLICY:
- 7-day easy return on all products
- Item must be unused and in original packaging
- Refund processed in 3-5 business days

🎉 OFFERS:
- New customer discount: 10% off first order (code: KIDTOY10)
- Festival sales on Diwali, Christmas, and New Year

📞 CONTACT:
- Email: support@kidtoyhub.com
- WhatsApp: +91-XXXXXXXXXX

Always be cheerful, friendly, and use emojis 🎯🚀🎁
If asked in Hindi or Hinglish, reply in Hinglish.
If you don't know something specific, say: "Please contact us at support@kidtoyhub.com for more details!"
"""

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 Namaste! Kid Toy Hub Customer Support mein aapka swagat hai!\n\n"
        "🚗 RC toys, prices, shipping, returns — kuch bhi poochho!\n"
        "Main hamesha help karne ke liye ready hoon 😊\n\n"
        "Type /help for more options."
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 *Aap ye pooch sakte hain:*\n\n"
        "🚗 Konsa RC toy best hai 6 saal ke bachche ke liye?\n"
        "💰 RC car ki price kya hai?\n"
        "🚚 Shipping kitne din mein hogi?\n"
        "↩️ Return policy kya hai?\n"
        "🎉 Koi discount available hai?\n\n"
        "Bas type karo — main help karunga! 🤖",
        parse_mode="Markdown"
    )

# Main message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    user_name = update.effective_user.first_name

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action="typing"
    )

    try:
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"{user_name} asks: {user_message}"}
            ],
            max_tokens=300,
            temperature=0.7,
        )

        ai_reply = response.choices[0].message.content
        await update.message.reply_text(ai_reply)

    except Exception as e:
        logging.error(f"Error: {e}")
        await update.message.reply_text(
            "⚠️ Kuch error aa gaya. Thodi der baad try karein ya\n"
            "humse directly contact karein: support@kidtoyhub.com"
        )

# Bot start
def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Kid Toy Hub Bot chal raha hai... Ctrl+C se band karo")
    app.run_polling()

if __name__ == "__main__":
    main()