import requests
import RunTTSbyDominik
import RunDictationByDominik

wiadomosc_bota = ""
input_path = 'Dictation.wav'
output_path = "TTS_PL.wav"
historia_rozmowy = open("historia.txt", "w")
while wiadomosc_bota != "Trzymaj się":
    RunDictationByDominik.audio_input()
    wiadomosc = RunDictationByDominik.asr(input_path)
    wiadomosc = wiadomosc[0]['transcript']
    print(wiadomosc)
    historia_rozmowy.write("\nUżytkownik:\n>" + wiadomosc)
    print("...")
    zapytanie = requests.post("http://localhost:5034/webhooks/rest/webhook", json={"message": wiadomosc})

    print("Bot mowi: ")
    for odpowiedz in zapytanie.json():
        if 'image' in odpowiedz.keys():
            wiadomosc_bota = odpowiedz['image']
        else:
            wiadomosc_bota = odpowiedz['text']
            RunTTSbyDominik.text2speech(output_path, wiadomosc_bota)
            RunTTSbyDominik.talk2us(output_path)


        print(wiadomosc_bota)
        historia_rozmowy.write("\nBot:\n>" + wiadomosc_bota)
historia_rozmowy.close()
