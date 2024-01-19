import telebot
from Conf import keys
from Token import token
from extensions import Conv, Exep

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message):
    text = "Для работы укажите запрос в следующем формате: \n<Иходная валюта> \
    <Желаемая валюта>\
    <Сумма>\n доступные валюты можно узнать по комманде: /values"
    bot.reply_to(message, text)
    pass

@bot.message_handler(commands=['values', ])
def handle_values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = "\n".join((text, key))
    bot.reply_to(message, text)
    pass

@bot.message_handler(content_types=["text",])
def fun(message: telebot.types.Message):
    try:
        val = message.text.split(" ")

        if len(val) != 3:
            raise Exep("Неверное заполнение переменных")

        queue, base, amount = val
        sum = Conv.convert(queue, base, amount )

    except Exep as e:
        bot.reply_to(message, f'ошибка пользователя \n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать комманду\n{e}')

    text = f"стоимость {amount} {queue} в {base} = {sum} {keys[base]}"
    bot.send_message(message.chat.id, text)
    pass

bot.polling(none_stop=True)
