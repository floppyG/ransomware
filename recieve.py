import socket

# Configurazione del server
indirizzo_locale = '0.0.0.0'  # Ascolta su tutte le interfacce di rete
porta = 12345

# Crea un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa il socket all'indirizzo e alla porta desiderati
server_socket.bind((indirizzo_locale, porta))

# Mette il server in modalità ascolto
server_socket.listen(1)

print(f"In ascolto su {indirizzo_locale}:{porta}...")

# Accetta la connessione in arrivo
connessione, indirizzo_client = server_socket.accept()
print(f"Connessione da {indirizzo_client}")

# Ricevi i dati dal client
dato_ricevuto = connessione.recv(1024).decode('utf-8')
print(f"Dato ricevuto: {dato_ricevuto}")

# Crea il file con la chiave
with open('thekey.key', 'w') as file_chiave:
    file_chiave.write(dato_ricevuto)
    print("File 'thekey.key' creato con successo.")

# Chiudi la connessione
connessione.close()
