import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import InputMediaPhoto
import gspread

bot = telebot.TeleBot('6910545174:AAEXz1VJKmqvm7F1C6zS_b0QQr2PkTGjweM');

@bot.message_handler(commands=['start'])
def start(message):
    if message.text == '/start':
       number_one = bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name} {message.from_user.last_name}, введите первое  число для совершения математической операции: ")
       bot.register_next_step_handler(number_one,number1_fun)


def number1_fun(message):
    global num1
    num1= message.text
    number_two = bot.send_message(message.chat.id , " введите второе число :")
    bot.register_next_step_handler(number_two, number2_fun)


def number2_fun(message):
    global num2
    num2=message.text
    operator = bot.send_message(message.chat.id, "Введите оператор(+,-,/,*):")
    bot.register_next_step_handler(operator,operators)


def operators(message):
    global operat
    oper = message.text
    if oper =="+":
        result = float(num1)+float(num2)
        bot.send_message(message.chat.id,result)
        bot.send_message(message.chat.id,"для повтора операции введите /start")
    elif oper == "-":
        result  = float(num1)-float(num2)
        bot.send_message(message.chat.id,result)
        bot.send_message(message.chat.id, "для повтора операции введите /start")
    elif oper == "*":
        result  = float(num1)*float(num2)
        bot.send_message(message.chat.id,result)
        bot.send_message(message.chat.id, "для повтора операции введите /start")
    elif oper == "/":
        result = float(num1)/float(num2)
        bot.send_message(message.chat.id,result)
        bot.send_message(message.chat.id, "для повтора операции введите /start")
    else:
        bot.send_message(message.chat.id,"Ошшибка ввода .Введите /start и повторите попытку")

print("Ready")
#bot.infinity_polling()
bot.polling(none_stop=True)