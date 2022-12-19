import requests

wiadomosc_bota = ""

while wiadomosc_bota != "Trzymaj się":
    wiadomosc = input("Twoje zapytanie:\n>")
    print("...")
    zapytanie = requests.post("http://localhost:5034/webhooks/rest/webhook", json={"message": wiadomosc})

    print("Bot mowi: ")
    for odpowiedz in zapytanie.json():
        wiadomosc_bota = odpowiedz['text']
        print(wiadomosc_bota)
