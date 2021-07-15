import requests
import schedule
import time
import dicts
from credentials import bot_token, bot_chatID
from datetime import date
from random import randint

def sendMessage(bot_message): 
    send = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}"    
    requests.get(send)


def sendSticker():
    sticker = "CAACAgEAAxkBAAMcYO8XlNk_8zFjppNE1zJDVy0H2RIAApwDAAKCgRcSHYIMX7KZMYwgBA"
    send = f"https://api.telegram.org/bot{bot_token}/sendSticker?chat_id={bot_chatID}&sticker={sticker}"
    requests.get(send)


def sendPhoto(img):
    send = f"https://api.telegram.org/bot{bot_token}/sendPhoto?chat_id={bot_chatID}&photo={img}"
    requests.get(send)


def msgCobrança():
    if date.today().day != 5:
        return
    hoje = date.today()
    sendMessage(f"Oi lindos, não gosto de cobrar e o bot tá fazendo o trabalho sujo 🤡")
    sendMessage(f"Hoje é a parcela de {dicts.meses.get(hoje.month)} do Alura, obrigado 🥰")
    sendSticker()


def msgEstudo():
    randomNum = randint(1,12)
    sendMessage(dicts.frases.get(randomNum))
    sendPhoto(dicts.imagens.get(randomNum))
    

# Mensagem ao ligar o bot
sendMessage("Estou funcionando, não se preocupa! (Agora com frases toda segunda!)")

schedule.every().day.at("08:00").do(msgCobrança)
# Para testar as mensagens de Estudo
#schedule.every().day.at("01:05").do(msgEstudo) 
schedule.every().monday.at("07:00").do(msgEstudo)

while True:
    schedule.run_pending()
    time.sleep(1)
