import telebot
from Dict import _dict
from Dict import token
from Dict import _list

bot = telebot.TeleBot(token)



@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if message.text in _dict:
        _message = _dict[message.text]
    else:
        _message = "Меня еще не научили ответу на этот вопрос 😕"

        _list.append(message.text)
        print(_list)

    bot.send_message(message.chat.id, _message)


if __name__ == '__main__':
    bot.infinity_polling()
