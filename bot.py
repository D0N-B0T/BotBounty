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


@bot.message_handler(commands=['tba'])
def tba_command(message):
    bot.send_message(message.chat.id, """
    →Seclists\n
    →Hash-identifier\n
    →XSSMAP\n
    →Smuggler\n
    →SSRFmap\n
    →Gmapsapiscanner\n
    →Qsreplace\n
    →exiftool\n
    →XSRFProbe\n
    →XXE Exploiter\n
    →Rush\n
    →Rustscan\n
    →LFISuite\n
    →Wapiti\n
    →Nuclei\n
    """)

#def domain command
@bot.message_handler(commands=['domain'])
def send_welcome(message):
    args = message.text
    send_welcome.args = args.split(' ')[1]
    bot.send_message(message.chat.id, "Running... Please wait.\n\n")
    bot.send_message(message.chat.id, "The whole process can take a while.\n\n")
    #process
    bot.send_message(message.chat.id, "[1] + Starting Sonar search with Rapid7.\n\n")
    send_welcome.process = sonar_rapid7()
    bot.send_message(message.chat.id, "[2] + Starting DNSX subdomain brute force.\n\n")
    send_welcome.process = dnsx()
    bot.send_message(message.chat.id, "[3] + Starting subdomain enumeration...")  
    send_welcome.process = subfinder()
    bot.send_message(message.chat.id, "[4] + Starting gau + unfurl.\n\n")
    send_welcome.process = gau()
    bot.send_message(message.chat.id, "[5] + Starting get ip address.\n\n")
    send_welcome.process = dnsx2()
    bot.send_message(message.chat.id, "[6] + Starting reverse dns.\n\n")
    send_welcome.process = rapid72()
    bot.send_message(message.chat.id, "[7] + Starting nrich portscan common cves.\n\n")
    send_welcome.process = shodan()
    bot.send_message(message.chat.id, "[8] + Starting portscan.\n\n")
    send_welcome.process = naabu()
    bot.send_message(message.chat.id, "[9] + Starting check active domains.\n\n")
    send_welcome.process = httpx_check()
    bot.send_message(message.chat.id, "[10] + Starting nuclei attack.\n\n")
    send_welcome.process = nuclei()
    bot.send_message(message.chat.id, "BotBounty work is done. Sending you the results.\n\n")
    #bot.send_document(message.chat.id, open(send_welcome.args + '.subfinder.txt', 'rb'))
    bot.send_message(message.chat.id, "Done. Now you can send me a new domain with /domain <url>.")
    



#0 sonar search tld
def sonar_rapid7():
    os.system('curl -k -s https://sonar.omnisint.io/subdomains/{args} | jq -r ‘.[]’ | sort -u > {args}.sonar.txt'.format(send_welcome.args, args=send_welcome.args))
    
#1 dnsx sub brute
def dnsx():
    os.system('dnsx -silent -d {args} -w -o {args}.dnsx.txt'.format(send_welcome.args, args=send_welcome.args))

#2 subfinder subdomain enumeration
def subfinder():
    #use args from start_process
    args = send_welcome.args
    #subprocess.call(['subfinder', '-d', args , '-o', args + '.subfinder.txt'])
    os.system('subfinder -d {args} -s -o {args}.subfinder.txt'.format(send_welcome.args, args=send_welcome.args))
    

#3 gau + unfurl
def gau():
    os.systen('gau {args} --blacklist png,jpg,gif -o {args}.gau.txt'.format(send_welcome.args, args=send_welcome.args))

#4 get ip address
def dnsx2():
    os.system('dnsx -silent -a -resp-only -l {args}.subfinder.txt'.format(send_welcome.args, args=send_welcome.args))


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
    os.system('nuclei ')




@bot.message_handler(commands=['astra'])
def getastra(message):
    bot.send_message(message.chat.id, "Running... Please wait.\n\n")
    #wait 1 second
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

@bot.message_handler(commands=['arjun'])
def getarjun(message):
    bot.send_message(message.chat.id, "Running... Please wait.\n\n")
    os.system('arjun -u {} -oT arjun.txt'.format(message.text[7:]))
    bot.send_document(message.chat.id, open('arjun.txt', 'rb'))
    os.system('rm arjun.txt')   
    bot.send_message(message.chat.id, "Done!")





bot.polling()

