import requests


def encrypt(data):
    url = "https://AntCrypt.whiteant.repl.co/antcrypt/v1/en"
    x = requests.post(url, data=data)
    return str(x.text)


def decrypt(data):
    url = "https://AntCrypt.whiteant.repl.co/antcrypt/v1/dec"
    x = requests.post(url, data=data)
    return str(x.text)

