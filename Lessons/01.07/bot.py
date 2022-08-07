#5473062923:AAESkXQOIXeno8s3DgN9M5M6HFQhubmNgWU

import telebot
from urllib.request import urlopen
from bs4 import BeautifulSoup

bot = telebot.TeleBot("5473062923:AAESkXQOIXeno8s3DgN9M5M6HFQhubmNgWU")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello!")

@bot.message_handler(commands=['update'])
def update_message(message):

    html = urlopen('https://kurs.onliner.by/')
    soup = BeautifulSoup(html)

    tag_list = soup.findAll('p', {'class':'value fall'})

    buy = tag_list[0].text
    sell = tag_list[1].text
    bot.send_message(message.chat.id, buy + ", " + sell)


bot.polling()

