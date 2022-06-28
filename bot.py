from multiprocessing.managers import SharedMemoryManager
import telebot
import secrets
import os

bot = telebot.TeleBot(secrets.TELEGRAM_TOKEN)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello, Im a Bug Bounty Bot.\nI can do the whole bounty thingy for you.\n\n")
    bot.send_message(message.chat.id, "To start, send me a domain with /domain <url>.\n\n")

@bot.message_handler(command="domain")
def start_process(message):
    args = message.text
    bot.send_message(message.chat.id, "Starting subdomain enumeration...")
    #user must send a domain as /domain <url>
    args = args.replace("/domain ", "")
    start_process.args = args
    start_process.process = subfinder()
    bot.send_message(message.chat.id, "Subdomain enumeration started.\n\n")


#0 sonar search tld
def sonar_rapid7():
    os.system('echo {} | rapid7 -o {}.rapid7.txt')

#1 dnsx sub brute
def dnsx():
    os.system('echo {} | dnsx -o {}.dnsx.txt')

#2 subfinder subdomain enumeration
def subfinder():
    os.system('echo {} | subfinder -d '+ start_process.args +'-o ~/BotBounty/'+ start_process.args +'.subdomians.txt')

#3 gau + unfurl
def gau():
    os.system('echo {} | gau -o {}.gau.txt')

#4 get ip address
def dnsx2():
    os.system('echo {} | dnsx2 -o {}.dnsx2.txt')

#5 reverse dns 
def rapid72():
    os.system('echo {} | rapid7 -o {}.rapid7.txt')

#6 nrich portscan common cves
def shodan():
    os.system('echo {} | shodan -o {}.shodan.txt')

#7 portscan
def naabu():
    os.system('echo {} | naabu -o {}.naabu.txt')

#8 check active domains
def httpx_check():
    os.system('echo {} | httpx3 -o {}.httpx3.txt')

#9 nuclei attack
def nuclei():
    os.system('echo {} | nuclei -o {}.nuclei.txt')




@bot.message_handler(commands=['astra'])
def getastra(message):

    #retrieve arg and send it to the astra script
    os.system('echo {} | python3 Astra.py > output.txt'.format(message.text[7:]))
    

    #if args start with http:// or https://, send it to the astra script
    arg = message.text[7:]
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

