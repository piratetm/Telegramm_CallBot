import telebot
from libs.zadarma import api


f = open('.its_master.txt')
if "true" in f.read():
    print("Ветка является мастером! Включаю основной токен!")
    bot = telebot.TeleBot('1661807622:AAEvPJrMSFILvWdE3ZTNi2gZ8ORYXYATdwc')
else:
    print("Ветка не является мастером! Включаю токен для тестирования!")
    bot = telebot.TeleBot('1658215806:AAETj5KBEi8Sv4wBnnrcKW7BY7zuuq9hoNk')

def zvonok_api():
    if __name__ == '__main__':
    z_api = api.ZadarmaAPI(key='YOU_KEY', secret='YOUR_SECRET')
    # get tariff information
    z_api.call('/v1/tariff/')
    # set callerid for your sip number
    z_api.call('/v1/sip/callerid/', {'id': '1234567', 'number': '71234567890'}, 'PUT')
    # get information about coast
    z_api.call('/v1/info/price/', {'number': '71234567891', 'caller_id': '71234567890'})


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')




bot.polling(none_stop=True)
