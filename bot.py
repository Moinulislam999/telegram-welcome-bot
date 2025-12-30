import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(
        message.chat.id,
        "👋 স্বাগতম!\n\n🌆 Image City Bot-এ আপনাকে স্বাগতম\n🖼️ AI Images | 🔥 Prompts | 🎁 Free Resources"
    )

bot.infinity_polling()
