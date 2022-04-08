import telebot
import config
import time

bot = telebot.TeleBot(config.TOKEN)

text = config.text

markup = telebot.types.InlineKeyboardMarkup()
markup1 = telebot.types.InlineKeyboardMarkup()
markup2 = telebot.types.InlineKeyboardMarkup()
markup3 = telebot.types.InlineKeyboardMarkup()

markup.add(telebot.types.InlineKeyboardButton('Рекламная съёмка', callback_data='Рекламная съёмка'))                                        #1
markup.add(telebot.types.InlineKeyboardButton('Свадебная съемка', callback_data='Свадебная съемка'))                                        #2
markup.add(telebot.types.InlineKeyboardButton('Репортажная съемка', callback_data='Репортажная съемка'))                                    #3
markup.add(telebot.types.InlineKeyboardButton('Студийная съемка', callback_data='Студийная съемка'))                                        #4
markup.add(telebot.types.InlineKeyboardButton('Интерьерная съемка', callback_data='Интерьерная съемка'))                                    #5
markup.add(telebot.types.InlineKeyboardButton('Работа с блогерами', callback_data='Работа с блогерами'))                                    #6
markup.add(telebot.types.InlineKeyboardButton('Love story и видеопортреты', callback_data='Love story и видеопортреты'))                    #7
markup.add(telebot.types.InlineKeyboardButton('Съемка мероприятий', callback_data='Съемка мероприятий'))                                    #8
markup.add(telebot.types.InlineKeyboardButton('Видеопоздравление с днем рождения', callback_data='Видеопоздравление с днем рождения'))      #9
markup.add(telebot.types.InlineKeyboardButton('Отзывы', callback_data='Отзывы'))                                                            #13

markup1.add(telebot.types.InlineKeyboardButton('Эконом', callback_data='Эконом'))                                                           #14
markup1.add(telebot.types.InlineKeyboardButton('Стандарт', callback_data='Стандарт'))                                                       #15
markup1.add(telebot.types.InlineKeyboardButton('Премиум', callback_data='Премиум'))                                                         #16

markup2.add(telebot.types.InlineKeyboardButton('Забронировать', callback_data='Забронировать'))                                             #17

markup3.add(telebot.types.InlineKeyboardButton('Слайд-шоу', callback_data='Слайд-шоу'))                                                     #10
markup3.add(telebot.types.InlineKeyboardButton('Профессиональная съёмка', callback_data='Профессиональная съёмка'))                         #11
markup3.add(telebot.types.InlineKeyboardButton('Музыкальный клип', callback_data='Музыкальный клип'))                                       #12

@bot.message_handler(commands =['start'])
def command2(message):
	bot.send_message(message.chat.id, text['Стартовое сообщение'] ,reply_markup=markup)

@bot.message_handler(commands =['reviews'])
def command1(message):
	bot.send_message(message.chat.id,'Отзывы: "ссылка на канал"')

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data != 'Забронировать':
        bot.edit_message_reply_markup(call.message.chat.id, message_id = call.message.message_id, reply_markup = '')

    if call.data == 'Забронировать': return #В будущем когда сделаем оплату надо убрать эту строку
    
    if call.data == 'Свадебная съемка':
        with open(f'img/{call.data}.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo,caption=text[call.data],reply_markup=markup1)

    elif call.data == 'Видеопоздравление с днем рождения':
        with open(f'img/{call.data}.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo,caption=text[call.data],reply_markup=markup3)

    elif call.data == 'Отзывы':
        bot.send_message(call.message.chat.id, 'Отзывы: "ссылка на канал"') 

    else:
        with open(f'img/{call.data}.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo,caption=text[call.data],reply_markup=markup2)


bot.polling(none_stop=True)