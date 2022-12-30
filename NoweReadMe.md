# **VoiceBot w Rasie**

## Do uruchomienia programu należy:
1. Pobierz pliki z naszego reporytorium 
2. Pobierz foldery dictation oraz tts z [repozytorium](https://github.com/marcinwitkowski/tm-clients.)
3. W pobranych folderach należy zmienić importy w plikach:
     <br>a) katalog dictation
    <br>
   - _dictation_client.py_
            `dictation.`
    <br>
   - _plik service_utils.py_
        `dictation.`
    <br>
   - _streaming_recognizer.py_
        `dictation.`
    <br>
   - _sync_recognizer.py_
        `dictation.`
    <br>
    <br>b) katalog tts, 
    <br> 
   -  _plik call_synthesize.py_
    <br>`import tts.techmo_tts_pb2 as techmo_tts_pb2              #alternatywa: from tts import techmo_tts_pb2
         import tts.techmo_tts_pb2_grpc as techmo_tts_pb2_grpc    #alternatywa: jw
         import grpc
         import os
         from tts.audio_player import AudioPlayer
         from tts.audio_saver import AudioSaver
         from tts.create_channel import create_channel`
    <br>
    - _plik techmo_tts_pb2_grpc.py_
	zamienić: "import techmo_tts_pb2 as techmo__tts__pb2", na "import tts.techmo_tts_pb2 as techmo__tts__pb2"
   <br>
    - _plik audio_saver.py_
	zamienić: "import techmo_tts_pb2", na `import tts.techmo_tts_pb2`
	<br>oraz wszystkie: "techmo_tts_pb2", na `tts.techmo_tts_pb2`
<br><br> 
4. Zainstaluj i włącz środowisko wirtualne
 <br>a) `python3 -m venv ./venv `      (bez 3, sam python)
 <br>b) `.\venv\Scripts\activate `      (jeśli nie działa, bo coś on this system, securityError, to      
`Set-ExecutionPolicy Unrestricted -Scope Process]` lub `cmd`
<br><br> 
5. Zainstaluj potrzebne pakiety (wszytskie reqirements.tx jakie są - spróbuje połaczyć w jedno)
	<br>`pip3 install -r requirements.txt` (bez 3, sam pip)
<br><br> 
6. Zainstaluj pakiet rasa
	<br>> `pip3 install rasa`
<br><br> 
7. W czasie instalacji stwórz z linków zamieszczonych na upelu plik addresses.json
<br><br>
8. Wytrenuj model
	`rasa train  `
9. Aktywacja API:
- Potrzebujemy 2 konsoli cmd w pycharmie (Jak poza pycharmem dziala inaczej to dajcie znac) wiec otwieramy terminal
   i plusikiem tworzymy drugi Local, w obu wpisujemy:
    cmd
- Dalej rozdziele konsole na A) i B), żeby oszczędzić sobie pisania. Ale w pkt 2. aktywujemy venva
    B i A) .\venv\Scripts\activate

- Włączamy rase w konsoli A)
    A) rasa run --enable-api --port 5034       (5034 to nr portu na jakim chcemu kominikowac sie z botem)

- Właczamy sobie api w konsoli B)
   B) python api_http.py                      (chodzi o to, że api musi byc wywołane w tym samym srodowisku co bot,
                                               jak ktos wie jak to zrobic inaczej niz z konsoli to dajcie prosze znac)                           

