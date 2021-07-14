import requests
import schedule
import time
from credentials import bot_token, bot_chatID
from datetime import date

def sendMessage(bot_message): 
    send = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}"
    
    requests.get(send)


def Mensagem():
    if date.today().day != 14:
        return
    hoje = date.today()
    sendMessage(f"Oi lindos, não gosto de cobrar e o bot tá fazendo o trabalho sujo 🤡")
    sendMessage(f"Hoje é a parcela de {meses.get(hoje.month)} do Alura, obrigado hihi")

meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro",
}

schedule.every().day.at("08:00").do(Mensagem)

while True:
    schedule.run_pending()
    time.sleep(1)

