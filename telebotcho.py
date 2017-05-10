import sys
import time
import telepot
from telepot.loop import MessageLoop
import config

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    print(msg['text'])

    if content_type == 'text':
        if 'hola bebotcho' in msg['text'].lower():
            bot.sendMessage(chat_id,'que pedal?')
        elif 'chinga tu madre bebotcho' in msg['text'].lower():
            bot.sendMessage(chat_id,'la tuya en vinagre!')
    else: 
        print('not text, srry')

TOKEN = config.token

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
