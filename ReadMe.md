# **VoiceBot w Rasie**

## Do uruchomienia programu należy:
1. Pobierz pliki z naszego reporytorium 
2. Pobierz foldery dictation oraz tts z [repozytorium](https://github.com/marcinwitkowski/tm-clients)
3. W pobranych folderach należy zmienić importy w plikach:
     <br>a) katalog dictation - należy dodać `dictation.` przed każdą ścieżką używanych plików jak na zdjęciu poniżej: 
     ![image](https://user-images.githubusercontent.com/84012463/210514571-3c30a804-36d4-4b9a-b983-3adc327ce78c.png)

    <br>
   - _dictation_client.py_
    <br>
   - _plik service_utils.py_
    <br>
   - _streaming_recognizer.py_
    <br>
   - _sync_recognizer.py_
    <br>
    <br>b) katalog tts, podobnie jak w poprzednim przed ścieżkami do plików trzeba dodać `tts.` 
    <br>
    <br> 
   -  _plik call_synthesize.py_
    <br> import tts.techmo_tts_pb2 as techmo_tts_pb2              #alternatywa: from tts import techmo_tts_pb2
    <br> import tts.techmo_tts_pb2_grpc as techmo_tts_pb2_grpc    #alternatywa: jw
    <br> import grpc
    <br> import os
    <br> from tts.audio_player import AudioPlayer
    <br> from tts.audio_saver import AudioSaver
    <br> from tts.create_channel import create_channel
    <br>
    - _plik techmo_tts_pb2_grpc.py_
	zamienić: "import techmo_tts_pb2 as techmo__tts__pb2", na "import tts.techmo_tts_pb2 as techmo__tts__pb2"
   <br>
    - _plik audio_saver.py_
	zamienić: "import techmo_tts_pb2", na `import tts.techmo_tts_pb2`
	<br>oraz wszystkie: "techmo_tts_pb2", na `tts.techmo_tts_pb2`
<br><br> 
4. Zainstaluj i włącz środowisko wirtualne (jeżeli nie działają poniższe linijki najeży spróbować skorzystać z instrukcji w tym linku: https://code.visualstudio.com/docs/python/python-tutorial)
 <br>
 <br>a) `python3 -m venv ./venv `      (bez 3, sam python)
 <br>b) `.\venv\Scripts\activate `      (jeśli nie działa, bo coś on this system, securityError, to      
`Set-ExecutionPolicy Unrestricted -Scope Process]` lub `cmd`
<br><br> 
5. Zainstaluj potrzebne pakiety (wszytskie reqirements.tx jakie są - spróbuje połaczyć w jedno)
	<br>`pip3 install -r requirements.txt` (bez 3, sam pip)
<br><br> 
6. W czasie instalacji stwórz z linków zamieszczonych na upelu plik addresses.json w ogólnym folderze VoiceBot-2.0
<br><br>
Wewnątrz paketu tkPDFViewer podmień linijki 46-48 na: <br>
                pix = page.get_pixmap()<br>
                pix1 = fitz.Pixmap(pix, 0) if pix.alpha else pix<br>
                img = pix1.tobytes("ppm")<br>
<br><br>	
7. Jeżeli w którymś z plików pojawia się błąd No module called: xxxxx 
oraz nie da się go zainstalować z poziomu programu należy to zrobić 
z poziomu cmd za pomocą funkcji pip install		
<br><br>
8. Wytrenuj model
	`rasa train  `
Sprawdź czy w folderze "models" pojawił się nowu plik modelu. Jeżeli nie powórz czynności.
<br><br> 
## Aktywacja API:
- Potrzebujemy 2 konsoli cmd w pycharmie (lub VS Code) wiec otwieramy terminal
   i plusikiem tworzymy drugi Local(albo prawym myszy i Split on Right) w obu wpisujemy:
    <br> `cmd`
 <br><br> 
- Dalej rozdziele konsole na A) i B), żeby oszczędzić sobie pisania. Ale w pkt 2. aktywujemy venva
    <br> B i A) `.\venv\Scripts\activate`
<br><br> 
- Włączamy rase w konsoli A)
  <br>  A) `rasa run --enable-api --port 5034`       (5034 to nr portu na jakim chcemu kominikowac sie z botem) 
  na tym etapie mogą pojawić się błędy jeżeli nie wszystkie pliki mają uzupełnione ścieżki. Będą wyświetlać się linki do plików którym trzeba je uzupełnić analogicznie jak w punkcie 3. 
<br><br> 
- Właczamy sobie api w konsoli dopiero kiedy rasa w konsoli A zostanie w pełni uruchomiona
   <br>B) `python main.py`                      (chodzi o to, że api musi byc wywołane w tym samym srodowisku co bot,
                                               jak ktos wie jak to zrobic inaczej niz z konsoli to dajcie prosze znac) 
<br><br> 
- Jeżeli pojawi się problem ffmpeg należy zakomentować warn w:
venv/Lib/pydub/utils.py -> linijka 165
- Jeżeli chcesz korzystać z asr no techmo `pip install git+https://github.com/openai/whisper.git `
- Jeżeli chcesz uruchomić bez dostępu do usług Techmo `python main.py --no-techmo`
