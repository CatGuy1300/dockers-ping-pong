import requests
import time

if __name__ == "__main__":
    while(True):
        r = requests.get('http://ping:5000/ping')
        time.sleep(1)
        print(r.text)