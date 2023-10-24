#!/usr/bin/python3

import os
import time
from base64 import *
from hashlib import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt(cle,txt):
  sel = os.urandom(16)
  cles = os.urandom(32)
  key = pbkdf2_hmac(',sha3_512',cles, sel, 100000, 32) 
  iv = os.urandom(AES.block_size)
  cipher = AES.new(key, AES.MODE_GCM, iv) 
  crypt_bytes = cipher.encrypt(pad(txt.encode(), AES.block_size))
  encrypted_text = b64encode(crypt_bytes).decode('utf-8)
  return encrypted_text, key.hex(), iv.hex()

def decrypt(key, encrypted_text, iv):
    cipher = AES.new(key, AES.MODE_GCM, iv)
    encrypted_bytes = b64decode(encrypted_text)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    decrypted_text = unpad(decrypted_bytes, AES.block_size).decode('utf-8')
    return decrypted_text
    
while True:
    print("1. Chiffrer")
    print("2. Déchiffrer")
    print("3. Quitter")
    choice = input("Choisissez une option: ")
    
    if choice == '1':
       cles = os.urandom(32)
       txt = input("Entrez votre texte: ")
       encrypted_text, key, iv = encrypt(cles, txt)
       print("Texte chiffrée: ", encrypted_text)
       print("Clé de chiffrement: ", key)
       print("IV de chiffrement: ", iv)
       
       
    elif choice == '2':
         encrypted_text = input("Entrez le texte chiffré: ")
         key = bytes.fromhex(input("Entrez la clé de chiffrement (en hexadécimal): "))
    
    
    
    
    
    
