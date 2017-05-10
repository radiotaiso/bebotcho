import sys
import time
import telepot
import random

from telepot.loop import MessageLoop
from foaas import fuck
#from pprint import pprint # Enable dis for debug!

import promesas
import config

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
#    print(content_type, chat_type, chat_id)
#    pprint(msg) # Debugging purposes

    if content_type == 'text':
        if 'hola bebotcho' in msg['text'].lower():
            bot.sendMessage(chat_id,'que tranza con Carranza? {}'.format(msg['from']['first_name']))
            # Que tranza con carranza <name>

        elif 'buenos d' in msg['text'].lower():
            bot.sendMessage(chat_id, 'buenos días {}'.format(msg['from']['first_name']))
            # Buenos días <name>

        elif 'bebotcho' and 'fml' in msg['text'].lower():
            fml = fuck.life(from_=msg['from']['first_name']).text
            bot.sendMessage(chat_id, fml)
            # Fuck my life - <name>

        elif 'uriel' and 'presidente' in msg['text'].lower():
            choice = random.choice(promesas.promesas_list)
            bot.sendMessage(chat_id, 'Cuando Uriel sea presidente: {}'.format(choice))
            # Cuando Uriel Sea Presidente <item de promesas.list>

    elif content_type != 'text': 
        print('not text, srry')
        # Handling things other than text

    else:
        print('wtf this is bad')
        # If this is ever printed we're you screwed up big time!

TOKEN = config.token

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Bot is alive and kicking ...')

# Keep the program running.
while 1:
    time.sleep(10)
