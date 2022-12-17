Do uruchomienia programu należy:

1. Pobierz pliki i zapisz w wybranym folderze
2. Dostań się do folderu
3. Windows: otwórz wiersz polecenia (cmd) i uruchom następujące polecenie:
	py -3 --version
4. Stwórz i aktywuj środowisko wirtualne
	py -3 -m venv .venv
	Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
	.venv\scripts\activate
#5. Zainstaluj potrzebne pakiety
		#C:\Users\Zosia\Desktop\ChatBot\.venv\Scripts\python.exe -m pip install --upgrade pip
	python -m pip install -r requirements.txt
6. Zainstaluj pakiet rasa
	pip3 install rasa
7. Wytrenuj model
	rasa train

w przypadku błedu daj znać Daniel Schnober (będziemy coś próbować poprawić)

8. Możesz zacząć korzystać z Chat bota
	rasa shell