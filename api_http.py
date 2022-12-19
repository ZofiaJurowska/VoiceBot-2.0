import requests

wiadomosc_bota = ""
historia_rozmowy = open("historia.txt", "w")
while wiadomosc_bota != "Trzymaj się":
    wiadomosc = input("Twoje zapytanie:\n>")
    historia_rozmowy.write("\nUżytkownik:\n>" + wiadomosc)
    print("...")
    zapytanie = requests.post("http://localhost:5034/webhooks/rest/webhook", json={"message": wiadomosc})

    print("Bot mowi: ")
    for odpowiedz in zapytanie.json():
        wiadomosc_bota = odpowiedz['text']
        print(wiadomosc_bota)
        historia_rozmowy.write("\nBot:\n>" + wiadomosc_bota)
historia_rozmowy.close()
