# Cobrador-Bot

Cobrador-Bot is a Telegram Bot that sends weekly and monthly a message in a group. You can customize which group, bot,  messages and images send. <br/>


## Setup
Clone this repository and config the **credentials .py** file.

To make it works, you need to register a bot and take his token to put in **bot_token**. (You can learn how to do it <a href="https://creativeminds.helpscoutdocs.com/article/2602-telegram-bot-telegram-creating-a-bot">**here**</a>)    
Also, you need to get the chatID to put in the **bot_chatID**, this will be the group (or person) that the bot will send messages. (Tutorial <a href="https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id">**here**</a>)

<img src="https://i.imgur.com/0S6CcsQ.png" width="60%" alt="Code inside credentials.py"/> <br/>

After that, check the **requeriments.txt** file and check if it is everything installed, that will be needed to run the bot. If its missing something, just run:

    pip install <Package>

With everything okay, just run the **main .py** file and let it running (or deploy that bot to a cloud server, but thats not the topic of this repo, check how to do it <a href="https://dev.to/josylad/how-to-deploy-a-python-script-or-bot-to-heroku-in-5-minutes-9dp">**here**</a>)

## Customize

The weekly message content and the images sent can be changed in the file **dicts.py**. <br/>

<img src="https://i.imgur.com/kFw2HP3.png" alt="Code inside dicts.py">

In the **frases** dict you can change directly the string that will be sent in the group, besides in  **imagens** you need to put the **file_id** code from the image. (You can learn how to get file_id from an image <a href="https://stackoverflow.com/questions/38106191/how-to-get-photo-in-real-size-not-thumb-from-telegram">**here**</a>)<br/>

PS: The index of *frases* dict will be the same of *imagens* when the bot send the message, so customize them together.
