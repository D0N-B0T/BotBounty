from multiprocessing.managers import SharedMemoryManager
import telebot
import secrets
import os
import subprocess 

bot = telebot.TeleBot(secrets.TELEGRAM_TOKEN)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello, Im a Bug Bounty Bot.\nI can do the whole bounty thingy for you.\n\n")
    bot.send_message(message.chat.id, "To start, send me a domain with /domain <url>.\n\n")



#def domain command
@bot.message_handler(commands=['domain'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Starting subdomain enumeration...")  
    args = message.text
    send_welcome.args = args.split(' ')[1]
    bot.send_message(message.chat.id, "Subdomain enumeration started.\n\n")
    send_welcome.process = subfinder()
    bot.send_message(message.chat.id, "Subdomain enumeration ended.\n\n")


#0 sonar search tld
def sonar_rapid7():
    return

#1 dnsx sub brute
def dnsx():
    return

#2 subfinder subdomain enumeration
def subfinder():
    #use args from start_process
    args = send_welcome.args
    subprocess.call(['subfinder', '-d', args , '-o', args + '.subfinder.txt'])
    os.system('subfinder -d {args} -o {args}.subfinder.txt'.format(send_welcome.args, args=send_welcome.args))
    

#3 gau + unfurl
def gau():
    return

#4 get ip address
def dnsx2():
    return

#5 reverse dns 
def rapid72():
    return

#6 nrich portscan common cves
def shodan():
    return

#7 portscan
def naabu():
    return

#8 check active domains
def httpx_check():
    return

#9 nuclei attack
def nuclei():
    return




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

