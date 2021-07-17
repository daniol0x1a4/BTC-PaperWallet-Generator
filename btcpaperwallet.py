
# Simple BTC Paper Wallet Generator.
# creates a PrivateKey and WalletAdress and outputs it as clear text and QRCode images
# {first little script after 2 days of learning python} ~ danielinfosec

from bitcoin import *
import qrcode

#(change out basekey value to create new wallet)
spaces = "----------------------------------------------"
basekey = "PUT IN YOUR RANDOM CHARACTERS FOR NEW WALLET ADRESS IN HERE"

#PrivateKey
print(spaces)
key1 = "PrivateKey"
print(key1)
priv = sha256 (basekey)
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

#PublicKey (Wallet) QRCode Adress
img = qrcode.make(addr)
img.save("publicwalletqr.png")
print("WalletAdress QR Code saved as publicwalletqr.png")
print(spaces)

#PrivateKey QRCode
img = qrcode.make(priv)
img.save("privatekey-qrcode.png")
print("PrivateKey QR Code saved as privatekey-qrcode.png")
print(spaces)


