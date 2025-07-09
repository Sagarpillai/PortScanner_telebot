import scanner
import telebot
from dotenv import load_dotenv
import os
import time
import json

load_dotenv()
api_token = os.getenv("API_TOKEN")
bot = telebot.TeleBot(api_token)

ip = None

@bot.message_handler(commands=['start','scan','result'])
def receive_message(message):
    global ip
    name = message.from_user.first_name
    welcome_text = """
    Hello! This is a port scanner bot 🔎, This bot scans the top 60 ports, This port scanner can only scan public IP's so don't enter private ip like 192.168.x.x It will not work\nUsage : /scan <ip>
    """
    if message.text == "/start":
        bot.reply_to(message,welcome_text)
    if "/scan" in message.text:
        bot.reply_to(message,"scanning ip ...")
        part = message.text.split(maxsplit=1)
        ip = part[1]
        if "192.168" in ip:
            bot.reply_to(message,"Can't scan the IP!\nas it is a local IP") 
        else:  
            scanner.scan_port(ip)
            time.sleep(15)
            if os.path.exists("open_ports.json"):
                bot.send_message(message.chat.id,"Scanning completed 💻\nto get result send /result")
    if message.text == "/result":
        if os.path.exists("open_ports.json"):
            with open("open_ports.json") as f:
                data = json.load(f)
            output = tree_view(ip, data)
            bot.send_message(message.chat.id, f"{output}")
            os.remove("open_ports.json")
        else:
            bot.send_message(message.chat.id,"Coudln't Load the output file 🌐")
    with open("user.log","a") as f:
        f.write(f"{name} : {time.ctime()}  \n")

def tree_view(ip, banners):
    ports = sorted(int(p) for p in banners)
    lines = [f"Scan result for {ip}"]
    for i, p in enumerate(ports):
        branch = "└─" if i == len(ports) - 1 else "├─"
        banner = banners[str(p)]
        lines.append(f"{branch} {p:<5} {banner}")
    return "\n".join(lines)


bot.polling()