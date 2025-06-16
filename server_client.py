import requests
import time
from bmp180 import get_readings

SERVER_URL = "http://<EC2_PUBLIC_IP>:5000/data" 

while True:
    try:
        data = get_readings()
        response = requests.post(SERVER_URL, json=data)
        print("Data sent:", data)
        print("Server response:", response.status_code)
    except Exception as e:
        print("Error sending data:", e)
    
    time.sleep(1) 

