Instrukcja instalacji oraz uruchomienia TTS:
1. Pobierz wymagane pliki z naszego repozytorium, oraz folder tts z https://github.com/marcinwitkowski/tm-clients

2. W popranych plikach, trzeba poszukać i zmienić importy. Te które pamiętam wypiałem poniżej, jeżeli coś pominąłem to
dopiszcie, proszę. Do zmiany:
    - katalog tts, plik call_synthesize.py
        import tts.techmo_tts_pb2 as techmo_tts_pb2              [alternatywa: from tts import techmo_tts_pb2]
        import tts.techmo_tts_pb2_grpc as techmo_tts_pb2_grpc    [alternatywa: jw]
        import grpc
        import os
        from tts.audio_player import AudioPlayer
        from tts.audio_saver import AudioSaver
        from tts.create_channel import create_channel
    - katalog tts, plik techmo_tts_pb2_grpc.py
	zamienić: "import techmo_tts_pb2 as techmo__tts__pb2", na "import tts.techmo_tts_pb2 as techmo__tts__pb2"
    - katalog tts, plik audio_saver.py
	zamienić: "import techmo_tts_pb2", na "import tts.techmo_tts_pb2"
	oraz wszystkie: "techmo_tts_pb2", na "tts.techmo_tts_pb2"

3. Jakby komuś pojawiał się błąd: ModuleNotFoundError: No module named 'tts.sounddevice' trzeba wpisać w terminal: pip install sounddevice  

4. Przejdź do Readme_api.txt i porozmiawiaj z naszym Botem
