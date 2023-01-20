import threading
import requests
import RunTTS
import RunDictation
import Question_GUI as q
import pyaudio
import wave
import webbrowser
import argparse
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.constants import DISABLED, NORMAL

# Sprawdzenie opcji uruchamiania
opcje_uruchamiania = argparse.ArgumentParser(description="Czy mamy polaczenie z Techmo?")
opcje_uruchamiania.add_argument("-t", "--techmo",   default=True, action=argparse.BooleanOptionalAction)
techmo = opcje_uruchamiania.parse_args().techmo

# Zmienne globalne
recording = False
is_image = False
input_path = "Dictation.wav"
output_path = "TTS_PL.wav"
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")
links = []
historia_rozmowy = open("historia.txt", "w")


def check_asr(input_file: [str or Path]):
    global techmo
    if techmo:
        wiadomosc = RunDictation.asr(input_file)
        return wiadomosc[0]['transcript']
    else:
        return RunDictation.no_techmo_asr(input_file)


def check_tts(out_path: [str or Path], output_text: str):
    global techmo
    if techmo:
        RunTTS.text2speech(out_path, output_text)
        RunTTS.talk2us(out_path)
    else:
        RunTTS.no_techmo_tts(output_text)


def zdjecie():
    global links
    for link in links:
        webbrowser.open_new_tab(link)


def image_button_state():
    global is_image
    if is_image:
        button_4["state"] = NORMAL
        is_image = False
    else:
        button_4["state"] = DISABLED


def record():
    canvas.delete("jeden")
    global historia_rozmowy, is_image, links
    # Nagrywanie
    buffer = 512
    fs = 16000
    format_audio = pyaudio.paInt16
    audio = pyaudio.PyAudio()
    stream = audio.open(format=format_audio, channels=1, rate=fs, input=True, frames_per_buffer=buffer)
    ramki = []
    while recording:
        data = stream.read(buffer)
        ramki.append(data)
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Zapisywanie pliku z nagraniem
    plik_dzwiekowy = wave.open(input_path, "wb")
    plik_dzwiekowy.setnchannels(1)
    plik_dzwiekowy.setsampwidth(audio.get_sample_size(format_audio))
    plik_dzwiekowy.setframerate(fs)
    plik_dzwiekowy.writeframes(b''.join(ramki))

    # Przekazanie wiadomości użytkownika do ASR
    wiadomosc = check_asr(input_path)
    historia_rozmowy.write("\nUżytkownik:\n>" + wiadomosc)
    canvas.create_text(
                        413,
                        217,
                        anchor="nw",
                        text=wiadomosc,
                        fill="#507255",
                        font=("Century Schoolbook", 30 * -1, 'bold'),
                        width=635,
                        tags="jeden"
                        )
    image_button_state()
    zapytanie = requests.post("http://localhost:5034/webhooks/rest/webhook", json={"message": wiadomosc})
    for odpowiedz in zapytanie.json():
        if 'image' in odpowiedz.keys():
            canvas.delete("dwa")
            canvas.delete("trzy")
            wiadomosc_bota = odpowiedz['image']
            is_image = True
            links.append(wiadomosc_bota)
            image_button_state()

        else:
            canvas.delete("dwa")
            canvas.delete("trzy")
            wiadomosc_bota = odpowiedz['text']
            canvas.create_text(
                                413,
                                415,
                                anchor="nw",
                                text=wiadomosc_bota,
                                fill="#507255",
                                font=("century schoolbook", 25 * -1),
                                width=635,
                                tags="trzy"
                                )
            check_tts(output_path, wiadomosc_bota)
        historia_rozmowy.write("\nBot:\n>" + wiadomosc_bota)


def click_handler():
    global recording
    if recording:
        record_button.config(image=button_image_1)
        print("Zakończono nagrywanie")
        recording = False

    else:
        record_button.config(image=button_image_2)
        print("Rozpoczęto nagrywanie")
        recording = True
        threading.Thread(target=record).start()


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Voice Bot")
window.iconbitmap("assets/frame0/image_3.ico")

window.geometry("1400x840")
window.configure(bg="#FEECEC")


canvas = Canvas(
                window,
                bg="#FEECEC",
                height=840,
                width=1400,
                bd=0,
                highlightthickness=0,
                relief="ridge"
                 )

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
                                775.5*1.4/1.5,
                                315.0*1.4/1.5,
                                image=image_image_1
                                )

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
                                749.0*1.4/1.5,
                                82.5*1.4/1.5,
                                image=image_image_2
                                )

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
                                194.5*1.4/1.5,
                                526.0*1.4/1.5,
                                image=image_image_3
                                )

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
                                780.0*1.4/1.5,
                                631.5*1.4/1.5,
                                image=image_image_4
                                )

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))

record_button = Button(
                        image=button_image_1,
                        borderwidth=0,
                        highlightthickness=0,
                        command=lambda: click_handler(),
                        relief="flat",
                        )
record_button.place(
                    x=(1171.5+100)*1.4/1.5,
                    y=757.5*1.4/1.5,
                    width=112.5*1.4/1.5,
                    height=112.5*1.4/1.5
                    )
canvas.create_text(
                    295.0*1.4,
                    348.0*1.4,
                    anchor="nw",
                    text="",
                    fill="#000000",
                    font=("Inter Regular", 18 * -1),
                    width=450,
                    tags="jeden"
                     )
canvas.create_text(
                    295.0*1.4,
                    348.0*1.4,
                    anchor="nw",
                    text="",
                    fill="#000000",
                    font=("Inter Regular", 18 * -1),
                    width=450,
                    tags="dwa"
                    )
canvas.create_text(
                    295.0*1.4,
                    348.0*1.4,
                    anchor="nw",
                    text="",
                    fill="#000000",
                    font=("Inter Regular", 18 * -1),
                    width=450,
                    tags="trzy"
                    )


image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
                                1322.0*1.4/1.5,
                                444.0*1.4/1.5,
                                image=image_image_5,
                                tags="7"
                                )

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
                    image=button_image_3,
                    borderwidth=0,
                    highlightthickness=0,
                    command=lambda: q.questions(),
                    relief="flat"
                    )
button_3.place(
                x=1425.0*1.4/1.5,
                y=22.499999999999996*1.4/1.5,
                width=60.0*1.4/1.5,
                height=60.0*1.4/1.5
                )

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(
                    image=button_image_4,
                    borderwidth=0,
                    highlightthickness=0,
                    command=zdjecie,
                    relief="flat"
                    )
button_4.place(
                x=131.5,
                y=707,
                width=105.0,
                height=105.0
                )
button_4["state"] = DISABLED

window.resizable(False, False)
window.mainloop()
historia_rozmowy.close()
