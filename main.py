from telebot import *
from config import *

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help'])
def richiesta_aiuto(message):
    user_name = message.from_user.first_name
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{user_name}, non ti preoccupare, il bot al momento funziona.")
    bot.send_message(chat_id,"Se non ti arriva la risposta vuol dire che probabilmente al momento WoZniaK è occupato.")

@bot.message_handler(commands=['start'])
def richiesta_chat(message):
    user_id =  message.from_user.id
    user_name = message.from_user.first_name
    chat_id = message.chat.id
    bot.send_message(chat_id, "Grazie per star utilizzando il mio bot.")
    bot.send_message(chat_id, "Dimmi tutto!")
    print(f"{user_name} -> START")

@bot.message_handler(content_types=["text","sticker","photo","audio","voice","video_note"])
def all(message):
    chat_id = message.chat.id
    if(chat_id != owner_chat_id):
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        message_id = message.message_id
        bot.forward_message(owner_chat_id,chat_id,message_id)
        bot.send_message(owner_chat_id, chat_id)
        print(f"{user_name} -> {nome_owner}")
    else:
        reply_to_message = message.reply_to_message
        if reply_to_message is None:
            bot.send_message(owner_chat_id, "Dovresti rispondere a un messaggio perchè funzioni.")
        else:
            try:
                message_id = message.message_id
                bot.forward_message(reply_to_message.text, owner_chat_id, message_id)
                print(f"{nome_owner} -> {reply_to_message.text}")
            except:
                bot.send_message(owner_chat_id, "Devi rispondere alla chat_id, non al messaggio.")
        


print("Bot online. | Dev by wozDev")

bot.polling()