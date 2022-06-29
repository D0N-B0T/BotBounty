#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
import secrets
import os

bot = telebot.TeleBot(secrets.TELEGRAM_TOKEN)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello, Im a Bug Bounty Bot.\nI can do the whole bounty thingy for you.\n\n")
    bot.send_message(message.chat.id, "To start, send me a domain with /domain <url>.\n\n")



#def domain command
@bot.message_handler(commands=['domain'])
def send_welcome(message):
    args = message.text
    send_welcome.args = args.split(' ')[1]
    bot.send_message(message.chat.id, "Running... Please wait.\n\n")
    bot.send_message(message.chat.id, "The whole process can take a while.\n\n")
    send_welcome.process = mkdir()
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
    bot.send_message(message.chat.id, "[6] + Starting crtsh.\n\n")
    send_welcome.process = crtsh() 
    bot.send_message(message.chat.id, "[7] + Starting nrich portscan common cves.\n\n")
    send_welcome.process = shodan_nrich()
    bot.send_message(message.chat.id, "[8] + Starting portscan.\n\n")
    send_welcome.process = naabu()
    bot.send_message(message.chat.id, "[9] + Starting check active domains.\n\n")
    send_welcome.process = httpx_check()
    bot.send_message(message.chat.id, "[10] + Starting nuclei attack.\n\n")
    send_welcome.process = nuclei()
    bot.send_message(message.chat.id, "BotBounty work is done. Sending now the results.\n\n")
    send_welcome.process = end()
    bot.send_message(message.chat.id, "Subdomains:\n\n")
    bot.send_document(message.chat.id, open('{args}/{args}.subdomains.txt'.format(args=send_welcome.args), 'rb'))
    bot.send_message(message.chat.id, "Links:\n\n")
    bot.send_document(message.chat.id, open('{args}/{args}.links.txt'.format(args=send_welcome.args), 'rb'))
    bot.send_message(message.chat.id, "IPs:\n\n")
    bot.send_document(message.chat.id, open('{args}/{args}.dnsx_ips.txt'.format(args=send_welcome.args), 'rb'))
    bot.send_message(message.chat.id, "Nuclei:\n\n")
    bot.send_document(message.chat.id, open('{args}/{args}.nuclei.txt'.format(args=send_welcome.args), 'rb'))
    


#? create directory if not exist
def mkdir():
    if not os.path.exists(send_welcome.args):
        os.system('mkdir {args}'.format(args=send_welcome.args))

#0 sonar search tld
def sonar_rapid7():
    os.system('curl -k -s https://sonar.omnisint.io/subdomains/{args} | jq -r ".[]" | sort -u > {args}/{args}.sonar.txt'.format(send_welcome.args, args=send_welcome.args))
    
#1 dnsx sub brute
def dnsx():
    os.system('dnsx -silent -d {args}/{args}.sonar.txt -w -o {args}/{args}.dnsx.txt'.format(send_welcome.args, args=send_welcome.args))

#2 subfinder subdomain enumeration
def subfinder():
    os.system('subfinder -silent -d {args} -o {args}/{args}.subfinder.txt'.format(send_welcome.args, args=send_welcome.args))
    
#3 gau + unfurl
def gau():
    os.system('gau {args} --blacklist png,jpg,gif --o {args}/{args}.gau.txt'.format(send_welcome.args, args=send_welcome.args))

#4 get ip address
def dnsx2():
    os.system('subfinder -silent -d bip.cl | dnsx -silent -a -resp-only -o {args}/{args}.dnsx_ips.txt'.format(send_welcome.args, args=send_welcome.args))

#5 get ctrsh
def crtsh():
    os.system('crtsh search --domain %.{args} --plain | anew > {args}/{args}.crtsh.txt'.format(send_welcome.args, args=send_welcome.args))

#6 nrich portscan common cves
def shodan_nrich():
    os.system('nrich {args}/{args}.dnsx_ips.txt -o {args}/{args}.cves_nrich.txt'.format(send_welcome.args, args=send_welcome.args))

#7 portscan
def naabu():
    os.system('naabu  -l {args}/{args}.subfinder.txt -s -o {args}/{args}.naabu.txt'.format(send_welcome.args, args=send_welcome.args))

#8 check active domains
def httpx_check():
    os.system('httpx -l {args}/{args}.subfinder.txt -silent -o {args}/{args}.httpx.txt'.format(send_welcome.args, args=send_welcome.args))

#9 nuclei attack
def nuclei():
    os.system('nuclei -o {args}/{args}.nuclei.txt'.format(send_welcome.args, args=send_welcome.args))

#end
def end():
    os.system('cat {args}/{args}.sonar.txt >> {args}/{args}.subtemp.txt'.format(send_welcome.args, args=send_welcome.args))
    os.system('cat {args}/{args}.crtsh.txt >> {args}/{args}.subtemp.txt'.format(send_welcome.args, args=send_welcome.args))
    os.system('cat {args}/{args}.subfinder.txt >> {args}/{args}.subtemp.txt'.format(send_welcome.args, args=send_welcome.args))
    os.system('cat {args}/{args}.subtemp.txt | anew  > {args}/{args}.subdomains.txt'.format(send_welcome.args, args=send_welcome.args))
    os.system('rm {args}/{args}.subtemp.txt'.format(send_welcome.args, args=send_welcome.args))
    os.system('cat {args}/{args}.gau.txt >> {args}/{args}.linktemp.txt'.format(send_welcome.args, args=send_welcome.args))
    os.system('cat {args}/{args}.httpx.txt >> {args}/{args}.linktemp.txt'.format(send_welcome.args, args=send_welcome.args))
    os.system('cat {args}/{args}.linktemp.txt | anew  > {args}/{args}.links.txt'.format(send_welcome.args, args=send_welcome.args))
    os.system('rm {args}/{args}.linktemp.txt'.format(send_welcome.args, args=send_welcome.args))








@bot.message_handler(commands=['nuclei'])
def getnuclei(message):
    bot.send_message(message.chat.id, "Running... Please wait.\n\n")
    send_welcome.process = nuclei()
    bot.send_document(message.chat.id, open(send_welcome.args + '.nuclei.txt', 'rb'))
    bot.send_message(message.chat.id, "Done.")


@bot.message_handler(commands=['astra'])
def getastra(message):
    bot.send_message(message.chat.id, "Running... Please wait.\n\n")
    os.system('echo {} | python3 Astra.py > output.txt'.format(message.text[7:]))
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






bot.infinity_polling(none_stop=True)