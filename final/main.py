import telebot

bot = telebot.TeleBot("5353535107:AAGZrjqxnQLOi2bAJpKqXeHxB6Iv3pdNYAg")


@bot.message_handler(commands=['/help'])
def handle_start_help():
    print("/help")
    print("/lowprice")
    print("/highprice")
    print("/bestdeal")
    print("/history")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "help":
        bot.send_message(message.from_user.id,
                         " You can use commands:\n help\n lowprice\n highprice\n bestdeal\n history")
    elif message.text == "lowprice":
        print("lowprice")
    elif message.text == "highprice":
        print("highprice")
    elif message.text == "bestdeal":
        print("bestdeal")
    elif message.text == "history":
        print("history")

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю.")


bot.polling(none_stop=True, interval=0)
