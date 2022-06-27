from multiprocessing.managers import SharedMemoryManager
import telebot
import secrets
import os

bot = telebot.TeleBot(secrets.TELEGRAM_TOKEN)


#subdomain enumeration
#active:
    #wordlist bruteforce
        #amass
    #permutational bruteforce
        #subbrute
    #virtual hosts
        #dnssearch

#passive
    #github
        #github subdomains
    #search engines
        #amass
        #assetfinder
        #subfinder
    #asn
        #nmap
        #httpx
        #amas intel -asn
    #ssl certs
        #crt.sh
        #crt_enum_psql.py
        #certspotter
    #hacker's search engines
        #shodan
            #shodan
            #shosubgo
        #censys
        #securitytrails
        #cloudflare
    #js parsing
        #httpx -> gospider
    #recursive enumeration
        #subdomains -> same tools






@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello, Im a Bug Bounty Bot.\nI can do the whole bounty thingy for you.\n\n")
    bot.send_message(message.chat.id, "To start, send me a domain.\n\n")



@bot.message_handler(commands=['astra'])
def getastra(message):
    arg = message.text[7:]
    #retrieve arg and send it to the astra script
    os.system('echo {} | python3 Astra.py > output.txt'.format(arg))

    #if args start with http:// or https://, send it to the astra script
    if arg.startswith('http://') or arg.startswith('https://'):
        if os.path.getsize('output.txt') > 4000:
            bot.send_message(message.chat.id, 'The output is too long to send in one message. I will send it as txt...')
            bot.send_document(message.chat.id, open('output.txt', 'rb'))
            os.remove('output.txt')            
        else:
            bot.send_message(message.chat.id, open('output.txt').read())
        bot.send_message(message.chat.id, "Done!")
    else:
        bot.send_message(message.chat.id, "Please enter a valid URL")

    

    

    



bot.polling()

