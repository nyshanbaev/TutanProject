import  telebot
import random
from env import TOKEN
bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('Yes')
button2 = telebot.types.KeyboardButton('No')
keyboard.add(button1, button2)




@bot.message_handler(commands=['start', 'hi'])
def start_function(message):
    # print(message.chat.id)
    msg = bot.send_message(message.chat.id, f"Hello {message.chat.first_name} let's play", reply_markup=keyboard)
    bot.register_next_step_handler(msg, answer_check)
    # bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJKCmOhPVvhoHeR4IIZZiQBbI29Vt4CAAKzAQACFkJrCnhafx6fPWbELAQ')
    # bot.send_photo(message.chat.id, 'https://pbs.twimg.com/profile_images/1528775264204906498/oufC8Yu8_400x400.jpg')
def answer_check(msg):
    if msg.text == 'Yes':
        bot.send_message(msg.chat.id, 'You have 3 chance, ugadai number from 1 to 10')
        random_number = random.randint(1,10)
        p = 3
        start_game(msg, random_number, p)
    else:
        bot.send_message(msg.chat.id, 'Bye!')
def start_game(msg, random_number, p):
    msg = bot.send_message(msg.chat.id, 'Enter number from 1 to 10: ')
    bot.register_next_step_handler(msg, check_func, p=p-1, random_number=random_number)
def check_func(msg, random_number, p):
    if msg.text == str(random_number):
        bot.send_message(msg.chat.id, 'You win!')
    elif p == 0:
        bot.send_message(msg.chat.id, f'You lose! Number was {random_number}')
    else:
        bot.send_message(msg.chat.id, f'Try noch ein mal, You have {p} chances')
        start_game(msg, random_number, p)
# @bot.message_handler()
# def echo_all(message):
#     bot.send_message(message.chat.id, message.text)


bot.polling()

"""
git init
git add .
git commit -m 'names commit'
git remote add origin ssh/https
git push origin master
"""