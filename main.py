from threading import Thread, Event

import telebot
from decouple import config
from flask import Flask, request, Response

TOKEN = config("TOKEN")
CHAT_ID = config("CHAT_ID")

app = Flask(__name__)
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    CHAT_ID = message.chat.id
    bot.reply_to(message, "Hey there, I will start sending notifications to you")


@bot.message_handler(commands=["ping"])
def send_response(message):
    bot.reply_to(message, "Hi, I am alive!")


@app.route("/api/webhook", methods=["POST"])
def echo_all():
    bot.send_message(CHAT_ID, f'{request.json["message"]}\n{request.json["url"]}')
    return None


@app.route("/api/ping")
def ping():
    return "telebot is running"


@app.route("/")
def index():
    bot.infinity_polling()
