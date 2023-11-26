#!/usr/bin/python3

###################################### Ajout de la fonction decrypt ############################################## 

def decrypt(key, encrypted_text, iv):
    cipher = AES.new(key, AES.MODE_GCM, iv)
    encrypted_bytes = b64decode(encrypted_text)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    decrypted_text = unpad(decrypted_bytes, AES.block_size).decode('utf-8')
    return decrypted_text

#################################################################################################################

