# This is a telegram bot progam that uses the module scanner that is created by me to scan the TOP 60 ports
# This program takes the result from the scanner module and sent the result back to the telegram bot

import scanner
import telebot
from dotenv import load_dotenv
import os
import time
import json

# loading the API tocken to establish the telegram connection it is obtained from @botfather in telegram
load_dotenv()
api_token = os.getenv("API_TOKEN")
bot = telebot.TeleBot(api_token)

ip = None # defining a global variable as it has no value currently assinging it null to avoid any overwrite collision

@bot.message_handler(commands=['start','scan','result'])
def receive_message(message):
    global ip
    name = message.from_user.first_name # storing the user name to store it to a log file for later check 
    welcome_text = """
    Hello! This is a port scanner bot 🔎, This bot scans the top 60 ports, This port scanner can only scan public IP's so don't enter private ip like 192.168.x.x It will not work\nUsage : /scan <ip>
    """ # welcome text saying the user what does the bot do
    if message.text == "/start":
        # if the command is "/start" then sending a welcome text
        bot.reply_to(message,welcome_text)
    if "/scan" in message.text:
        # perfroming a scan if the command "/scan" is send
        bot.reply_to(message,"scanning ip ...")
        part = message.text.split(maxsplit=1)
        ip = part[1] # taking the IP part from the command
        if "192.168" in ip:
            # checking if it is a local IP
            bot.reply_to(message,"Can't scan the IP!\nas it is a local IP") 
        else:  
            scanner.scan_port(ip)
            time.sleep(15) # giving time for the scanner to complete scan and get output
            if os.path.exists("open_ports.json"):
                # cheking if the output file is present 
                bot.send_message(message.chat.id,"Scanning completed 💻\nto get result send /result")
    if message.text == "/result":
        if os.path.exists("open_ports.json"):
            with open("open_ports.json") as f:
                data = json.load(f)
            output = tree_view(ip, data) # making the json file content into a representable mode
            bot.send_message(message.chat.id, f"{output}") # sending the modified scanning result to the telegram user
            os.remove("open_ports.json") # removing the json after sending the contents
        else:
            bot.send_message(message.chat.id,"Coudln't Load the output file 🌐")
    with open("user.log","a") as f:
        # takin the note of users that used the telegram bot
        f.write(f"{name} : {time.ctime()}  \n")

def tree_view(ip, banners):
    # program to modify the json to a representable mode
    ports = sorted(int(p) for p in banners)
    lines = [f"Scan result for {ip}"]
    for i, p in enumerate(ports):
        branch = "└─" if i == len(ports) - 1 else "├─"
        banner = banners[str(p)]
        lines.append(f"{branch} {p:<5} {banner}")
    return "\n".join(lines)


bot.polling() # Used for reading the user input messages
