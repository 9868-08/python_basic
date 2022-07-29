import os
import configparser
import telebot
import requests

config = configparser.ConfigParser()
config.read('config.ini')
TOKEN=config.get("DEFAULT", "TOKEN")
user_id=config.get("DEFAULT", "iser_id")
#print(TOKEN, user_id)
#bot = telebot.TeleBot("5353535107:AAGZrjqxnQLOi2bAJpKqXeHxB6Iv3pdNYAg")
bot = telebot.TeleBot(TOKEN)

def lowprice():
    url = "https://hotels4.p.rapidapi.com/locations/v2/search"
    querystring = {"query": "new york", "locale": "en_US", "currency": "USD"}
    headers = {
        "X-RapidAPI-Key": "a66df32f87mshe86994164d3c458p18029djsnb52f634dfcfe",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring, timeout=10)
    data = json.loads(response.text)  # десериализация JSON
#    hotels = response.text
    print(response.text)
    return "response.text"

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "help":
        bot.send_message(message.from_user.id,
                         " You can use commands:\n help\n lowprice\n highprice\n bestdeal\n history")
    elif message.text == "lowprice":
#        bot.send_message(message.from_user.id, "you input - lowprice")
        bot.send_message(message.from_user.id, lowprice())

    elif message.text == "highprice":
        bot.send_message(message.from_user.id, "you input - highprice")
    elif message.text == "bestdeal":
        bot.send_message(message.from_user.id, "you input - bestdeal")
    elif message.text == "history":
        print("you input - history")

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю.")



bot.polling(none_stop=True, interval=5)
