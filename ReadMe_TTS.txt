Instrukcja instalacji oraz uruchomienia TTS:
1. Pobierz wymagane pliki.

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

3. Przejdź do Readme_api.txt i porozmiawiaj z naszym Botem