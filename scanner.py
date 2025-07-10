# This is a TCP protocol port scanning program that scans for open ports
# This scans the top 60 ports in the taget system 
# This program also try to grab the banner but only of TCP connection and if can't grab the banner returns the string banner not grabed
# This is an educational program use this for educational uses and the author is not liable for any unethical use

import socket
import json


def banner_grab(ip,open_port):
    # function to grab banner
    banners = {}
    for ports in open_port:
        udp_ports = [53,67,68,69,88,123,161,162,500,520]
        if ports in udp_ports: # avoiding the UDP ports as it requires UDP protocol and this pogram only uses TCP protocol for scanning
            banners.update({ports : "UDP port/Can't fetch banner"})
            continue
        else:
            try:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
                s.settimeout(1)
                s.connect((ip,ports))
                banner = s.recv(1024).decode().strip()
                banners.update({ports : banner})
            except:
                banners.update({ports : "No Banner"})
            finally:
                s.close() # closing the earlier created connection and creating a new one
    save_json(banners) # saving all the obtained banners and there respective ports to a json file


def save_json(banners):
    # function used to create a json file from the open ports and the banners grabed from them
    with open("open_ports.json","w") as f:
        # using the write mode to always over write the file rather than appending 
        f.write(json.dumps(banners))


def scan_port(ip):
    imp_port = [7,20,21,22,23,25,53,69,80,88,102,110,135,137,139,143,381,443,464,465,587,593,636,691,902,989,990,995,1025,1194,1337,1589,1725,2082,2083,2483,2967,3074,3306,3724,4444,4664,5432,5900,6665,6666,6667,6668,6669,6881,6999,6970,8086,8087,8222,9100,10000,12345,27374,31337]
    # the list of most common 60 ports
    open_port = []
    for ports in imp_port:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(0.5)
        signal = s.connect_ex((ip,ports)) # getting the signal from the port with a settimeout as it scans the ports only for a that time
        if signal == 0:
            open_port.append(ports)
        s.close()
    banner_grab(ip,open_port) # calling the banner grab function to get the banner of the open ports
