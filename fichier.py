#!/usr/bin/python3

import os
from base64 import * 
import time 
from haslib import * 
from Crypto.Cipher.Padding import pad, unpad 

def encrypt(cle,txt):
  sel = os.urandom(16)
  cles = os.urandom(32)
  key = pbkdf2_hmac(',sha3_512',cles, sel, 100000, 32) 
  iv = os.urandom(AES.block_size)
  cipher = AES.new(key, AES.MODE_GCM, iv) 
  crypt_bytes = cipher.encrypt(pad(txt.encode(), AES.block_size))
  encrypted_text = b64encode(crypt_bytes).decode('utf-8)
  return encrypted_text, key.hex(), iv.hex()