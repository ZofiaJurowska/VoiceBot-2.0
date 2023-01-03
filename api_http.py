import threading

import requests
import RunTTSbyDominik
import RunDictationByDominik
import pyaudio
import wave
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

global wiadomosc_bota
wiadomosc_bota = ""
global wiadomosc
wiadomosc = ""
global zapytanie
zapytanie = requests.post("http://localhost:5034/webhooks/rest/webhook", json={"message": wiadomosc})


input_path = 'Dictation.wav'
output_path = "TTS_PL.wav"
historia_rozmowy = open("historia.txt", "w")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


global recording
recording = True

global stream, audio, ramki, out_path, fs, format_audio
out_path:[str or Path]="Dictation.wav"
buffer:int=512
fs:int=16000
format_audio = pyaudio.paInt16

def record():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=format_audio, channels=1, rate=fs, input=True, frames_per_buffer=buffer)
    ramki = []
    while recording:
        data = stream.read(buffer)
        ramki.append(data)
    stream.stop_stream()
    stream.close()
    audio.terminate()

    plik_dzwiekowy = wave.open(out_path, "wb")
    plik_dzwiekowy.setnchannels(1)
    plik_dzwiekowy.setsampwidth(audio.get_sample_size(format_audio))
    plik_dzwiekowy.setframerate(fs)
    plik_dzwiekowy.writeframes(b''.join(ramki))

    global wiadomosc
    wiadomosc = RunDictationByDominik.asr(input_path)
    wiadomosc = wiadomosc[0]['transcript']
    historia_rozmowy.write("\nUżytkownik:\n>" + wiadomosc)
    global zapytanie
    zapytanie = requests.post("http://localhost:5034/webhooks/rest/webhook", json={"message": wiadomosc})
    for odpowiedz in zapytanie.json():
        if 'image' in odpowiedz.keys():
            wiadomosc_bota = odpowiedz['image']
        else:
            wiadomosc_bota = odpowiedz['text']
            RunTTSbyDominik.text2speech(output_path, wiadomosc_bota)
            RunTTSbyDominik.talk2us(output_path)

        historia_rozmowy.write("\nBot:\n>" + wiadomosc_bota)


def click_handler():
    global recording
    if recording:
        record_button.config(image=button_image_1)
        print("JUŻ NIE NAGRYWAM")
        recording = False

    else:
        record_button.config(image=button_image_2)
        print("JAZDA")
        recording= True
        threading.Thread(target=record).start()


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Voice Bot by Dominik")
window.iconbitmap("assets/frame0/image_3.ico")

window.geometry("1000x600")
window.configure(bg = "#FEECEC")


canvas = Canvas(
    window,
    bg = "#FEECEC",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    517.0,
    210.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    499.0,
    55.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    130.0,
    351.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    520.0,
    421.0,
    image=image_image_4
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))

record_button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click_handler(),
    relief="flat"
)
record_button.place(
    x=848.0,
    y=505.0,
    width=75.0,
    height=75.0
)

canvas.create_text(
    292.0,
    136.0,
    anchor="nw",
    text= wiadomosc,
    fill="#000000",
    font=("Inter Regular", 20 * -1)
)

canvas.create_text(
    295.0,
    348.0,
    anchor="nw",
    text= wiadomosc_bota,
    fill="#000000",
    font=("Inter Regular", 20 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    881.0,
    296.0,
    image=image_image_5
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=950.0,
    y=14.999999999999996,
    width=40.0,
    height=40.0
)

window.resizable(False, False)

#while wiadomosc_bota != "Trzymaj się":

window.mainloop()
historia_rozmowy.close()
'''
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

        zapiszOdpowiedzBota(wiadomosc_bota)
        print(wiadomosc_bota)
        historia_rozmowy.write("\nBot:\n>" + wiadomosc_bota)
historia_rozmowy.close()
'''