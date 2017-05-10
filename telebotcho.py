import sys
import time
import telepot
from telepot.loop import MessageLoop
import config
from pprint import pprint
from foaas import fuck

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    pprint(msg)

    if content_type == 'text':
        if 'hola bebotcho' in msg['text'].lower():
            bot.sendMessage(chat_id,'que tranza con Carranza? {}'.format(msg['from']['first_name']))
        elif 'buenos d' in msg['text'].lower():
            bot.sendMessage(chat_id, 'buenos días {}'.format(msg['from']['first_name']))
        elif 'chingas' or 'chinga' and 'bebotcho' in msg['text'].lower():
            response = fuck.you(name=msg['from']['first_name'], from_='Bebotcho').text
            bot.sendMessage(chat_id, response)
    else: 
        print('not text, srry')

TOKEN = config.token

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
