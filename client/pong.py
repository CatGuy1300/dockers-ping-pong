import requests

if __name__ == "__main__":
    r = requests.get('http://ping:5000/ping')
    print(r.text)