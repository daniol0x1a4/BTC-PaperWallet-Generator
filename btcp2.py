# daniol0xA41
# Version no.2 btcpaperwallet

import os
import time 
from bitcoin import *
import qrcode
import string
import random
import pyfiglet

def starttext():
    btc = pyfiglet.figlet_format("BTCp2")
    os.system("clear")
    print(btc)
starttext()

letters = string.ascii_letters + string.digits + string.ascii_lowercase + string.punctuation
crypto =  ''.join(random.choice(letters) for i in range(10000)) 

def spaces():
    id = "------------------------------------------------------------"
    print(id)

def c():
    spaces()
    print("PrivateKey:")
    priv = sha256 (crypto)
    print(priv)
    spaces()
    pub = privtopub(priv)
    key3 = ("WalletAdress:")
    print(key3)
    addr = pubtoaddr(pub)
    print(addr)
    spaces()
    print("\n")
    img = qrcode.make(addr)
    img.save("publicwalletqr.png")
    img = qrcode.make(priv)
    img.save("privatekey-qrcode.png")
c()
