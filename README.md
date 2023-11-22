# ransomware
this programm is capable of encrypting any file within the directory in which it is detonated, automatically sending the key for decryption to the attacker in the same network as the victim.<br>
Upon payment of the ransom, the attacker will tell the victim to start recive.py to open the ftp port and receive the key for decryption from the attacker.

## the victim need to have: 
        ransomware.py        -> encrypt all the data 
        decrypt.py           -> decrypt all the data using the same key            
        recieve.py           -> used to recive the key from the attacker

## the attacker need to have
        listener.py           -> must remain listening because as soon as the ransomware is started, it automatically sends the key to the attacker
        send.py               -> used to send the key for decrypting to the victim
