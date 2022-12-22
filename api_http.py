import requests
import RunTTSbyDominik

wiadomosc_bota = ""
output_path = "TTS_PL.wav"
historia_rozmowy = open("historia.txt", "w")
while wiadomosc_bota != "Trzymaj się":
    wiadomosc = input("\nTwoje zapytanie:\n>")
    historia_rozmowy.write("\nUżytkownik:\n>" + wiadomosc)
    print("...")
    zapytanie = requests.post("http://localhost:5034/webhooks/rest/webhook", json={"message": wiadomosc})

    print("Bot mowi: ")
    for odpowiedz in zapytanie.json():
        if 'image' in odpowiedz.keys():
            wiadomosc_bota = odpowiedz['image']
        else:
            wiadomosc_bota = odpowiedz['text']
        print(wiadomosc_bota)

        RunTTSbyDominik.text2speech(output_path, wiadomosc_bota)
        RunTTSbyDominik.talk2us(output_path)

        historia_rozmowy.write("\nBot:\n>" + wiadomosc_bota)
historia_rozmowy.close()
