import requests
import json


wiadomosc_bota = ""

while wiadomosc_bota != "Trzymaj się":
    wiadomosc = input("Twoje zapytanie:\n>")
    print("...")
    zapytanie = requests.post("http://localhost:5034/webhooks/rest/webhook", json={"message": wiadomosc})

    print("Bot mowi: ")
    for cos in zapytanie:
        wiadomosc_bota = json.loads(cos)
        for item in wiadomosc_bota:
            print(item['text'])

