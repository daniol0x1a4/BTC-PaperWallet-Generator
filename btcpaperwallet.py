from bitcoin import *
import qrcode
import string 
import random

spaces = "----------------------------------------------"
letters = string.ascii_letters + string.digits + string.ascii_lowercase + string.punctuation
crypto =  ''.join(random.choice(letters) for i in range(10000)) 

#PrivateKey
print(spaces)
key1 = "PrivateKey"
print(key1)
priv = sha256 (crypto)
print(priv)
print(spaces)

#PublicKey
pub = privtopub(priv)

#WalletAdress
key3 = ("WalletAdress")
print(key3)
addr = pubtoaddr(pub)
print(addr)
print(spaces)

img = qrcode.make(addr)
img.save("publicwalletqr.png")

img = qrcode.make(priv)
img.save("privatekey-qrcode.png")


