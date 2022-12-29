Instrukcja instalacji oraz uruchomienia ASR:
1. Pobierz wymagane pliki (wszytskie pliki, które są w repozytorium a nie masz ich u siebie, lub zostały
    zmienione(api_http.py na 100%)), oraz folder dictation z https://github.com/marcinwitkowski/tm-clients.

2. W popranych plikach, trzeba poszukać i zmienić importy. Te które pamiętam wypisałem poniżej, jeżeli coś pominąłem to
dopiszcie, proszę. Tam gdzie brakuje trzeba dokleić "dictation."
-katalog dictation, plik dictation_client.py
    dictation.

-katalog dictation,
    -plik service_utils.py
        dictation.

    -streaming_recognizer.py
        dictation.

    -sync_recognizer.py
        dictation.


3. Wpisz w (venv), jeśli nie jest aktywowane, to trzeba katywować
    pip install -r .\dictation\requirements.txt

4. Przejdź do Readme_api.txt i porozmiawiaj z naszym Botem

