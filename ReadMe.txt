#VoiceBot w Rasie

##Do uruchomienia programu należy:

1. Pobierz pliki i zapisz w wybranym folderze
1. Dostań się do folderu
1. Windows: otwórz wiersz polecenia (cmd) i uruchom następujące polecenie:
   ```shell
	py -3 --version
  '''
1. Stwórz i aktywuj środowisko wirtualne
  '''shell
	py -3 -m venv .venv
	Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
	.venv\scripts\activate
  '''
#5. Zainstaluj potrzebne pakiety
	#C:\Users\Zosia\Desktop\ChatBot\.venv\Scripts\python.exe -m pip install --upgrade pip
  '''shell  
	python -m pip install -r requirements.txt
  '''
6. Zainstaluj pakiet rasa
'''shell
	pip3 install rasa
  '''
7. Wytrenuj model
'''shell
	rasa train
'''
w przypadku błedu daj znać Daniel Schnober (będziemy coś próbować poprawić)

8. Możesz zacząć korzystać z Chat bota
  '''shell
	rasa shell
  '''
