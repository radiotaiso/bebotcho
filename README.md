# Welcome to Bebotcho's guts
This is a cool recipe to create your own kickass bot.



## Bebotcho's origins..
So, I wanted to create a telegram bot to joke around, here is the result.
This is somewhat an ongoing project so I'm sure it will be broken from time to time.
Most interaction is in spanish, feel free to fork it and change whatever the hell you want.

## How to kickstart the bot
* You'll need your own telgram bot token (you can make your own using @Botfather)
* Create `config.py` file and just put there `token = 'your_token_goes_here'`.
* Go to your favorite terminal, enable the virtualenv and `python telebotcho.py`.

There you go.

### Say hi to bebocho!
If you say `Hola bebotcho` he will answer back!

### Good morning sunshine!
Same way as before but this time the trigger is anything that contains `buenos d` (as in `buenos días` in spanish) I was too lazy to regex this shit, maybe in the future.

### Fuck off as a service!
Using the [FOAAS python wrapper](https://github.com/dmpayton/foaas-python), Bebotcho knows when life sucks! just tell him anything containing `fml` and `bebotcho` in the same message.

#### Everything else
Big kudos to the python wrapper for Telegram API [Telepot](https://github.com/nickoala/telepot) and [Fuck Off As A Service](https://www.foaas.com/)!

