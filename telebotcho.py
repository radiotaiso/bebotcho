import sys
import time
import telepot
from telepot.loop import MessageLoop
import config
from pprint import pprint
from foaas import fuck
import promesas

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    pprint(msg)

    if content_type == 'text':
        if 'hola bebotcho' in msg['text'].lower():
            bot.sendMessage(chat_id,'que tranza con Carranza? {}'.format(msg['from']['first_name']))
        elif 'buenos d' in msg['text'].lower():
            bot.sendMessage(chat_id, 'buenos días {}'.format(msg['from']['first_name']))
#        elif 'fuck you bebotcho' or 'fuck u bebotcho' in msg['text'].lower():
#            fu = fuck.you(name=msg['from']['first_name'], from_='Bebotcho').text
#            bot.sendMessage(chat_id, fu)
        elif 'bebotcho fml' in msg['text'].lower():
            fml = fuck.life(from_=msg['from']['first_name']).text
            bot.sendMessage(chat_id, fml)
        elif 'uriel' and 'presidente' in msg['text'].lower():
            rand_promis = campaign.promis
            bot.sendMessage(chat_id, 'Cuando Uriel sea presidente {}'.format(rand_promis))

    elif content_type != 'text': 
        print('not text, srry')
    else:
        print('wtf this is bad')

TOKEN = config.token

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
