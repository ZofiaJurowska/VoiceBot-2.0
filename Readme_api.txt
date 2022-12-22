Instalacja sprowadza się do pobrania pliku api-http.py do folderu z projektem oraz skopiowania ponizszego kodu
do pliku credentials.yml (ja wkleilem na koncu)
    callback:
        # URL to which Core will send the bot responses
        url: "http://localhost:5034/bot"                     [5034 to nr portu na jakim chcemu kominikowac sie z botem]

========================================================================================================================
Aktywacja API:
1) Potrzebujemy 2 konsoli cmd w pycharmie (Jak poza pycharmem dziala inaczej to dajcie znac) wiec otwieramy terminal
   i plusikiem tworzymy drugi Local, w obu wpisujemy:
    cmd
2) Dalej rozdziele konsole na A) i B), żeby oszczędzić sobie pisania. Ale w pkt 2. aktywujemy venva tu i tu
    B i A) .\venv\Scripts\activate

3) Włączamy rase w konsoli A)
    A) rasa run --enable-api --port 5034       [5034 to nr portu na jakim chcemu kominikowac sie z botem]

4) Właczamy sobie api w konsoli B)
    B) python api_http.py                      [chodzi o to, że api musi byc wywołane w tym samym srodowisku co bot,
                                               jak ktos wie jak to zrobic inaczej niz z konsoli to dajcie prosze znac]