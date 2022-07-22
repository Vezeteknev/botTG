import telebot # конект с библиотекой телеграмма. 

from telebot import types#подключаемся к библиотеке types
 
bot =telebot.TeleBot('')# установка токена бота 

@bot.message_handler(commands=['start'])# рассматриваем команду start
#отслеживание команд
def start(message):# функция по написанию сообщения юзеру 
    mess= f'Салам брат <b> <u>{message.from_user.first_name}{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')# отправляет сообщение 

#создаем кнопку 
@bot.message_handler(commands=['translation'])

def website(message):
    button = types.InlineKeyboardMarkup(row_width=3)  
    button.add(types.InlineKeyboardButton("заходи", url="https://yandex.ru/search/?text=%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4%D1%87%D0%B8%D0%BA&lr=54&clid=2411726"))
    bot.send_message(message.chat.id, "смотри че нашел" , reply_markup=button)

#создаем клавиатуру 
@bot.message_handler(commands=['keyboard'])
def keyboard(message):
    button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)# resize_keyboard=true, что бы выглядело топого,под ровный размер, row_width-ширина ряда(в одном ряду по 1 кнопк итд)

    translation= types.KeyboardButton('/translation')
    start= types.KeyboardButton("/start")
   
    button.add(translation, start)
    
    bot.send_message(message.chat.id,'хавай', reply_markup=button)
#обработка текста
@bot.message_handler() #рассматривает текст 
def get_user_text(message):
 if message.text == "алейкум Асалям":
    bot.send_message(message.chat.id, 'я уже поздаровался ', parse_mode='html')
 elif message.text == "id":
     bot.send_message(message.chat.id, f'Вот твой ID {message.from_user.id}', parse_mode='html')
 elif message.text == "фото":
   photo = open('315437.png', 'rb')#отправка файлов
   bot.send_photo(message.chat.id, photo)
   
 else:
     bot.send_message(message.chat.id, 'я ща ниче не понял ', parse_mode='html')

#обработка файла
@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Ну и  зачем это мне?...")


    

bot.polling(none_stop=True)