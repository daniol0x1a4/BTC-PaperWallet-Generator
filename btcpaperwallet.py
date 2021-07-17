
# Simple BTC Paper Wallet Generator.
# creates a PrivateKey and WalletAdress and outputs it as clear text and QRCode images
# {first little script after 2 days of learning python} ~ danielinfosec

from bitcoin import *
import qrcode

#(change out basekey value to create new wallet)
spaces = "----------------------------------------------"
basekey = "KHDtL33NLT65p5DjogY$NxgCiJ4F5TqbJ?8cr#5@iegfhqqoifoih56i&/%NF(WDJ7839ß302842ß4082ß408y#BC7RPShFTa#r6!RbkqQhG5YkGk9snTa4px$q9f"

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
print("Public Adress QR Code succesfull saved as publicwalletqr.png")
print(spaces)

#PrivateKey QRCode
img = qrcode.make(priv)
img.save("privatekey-qrcode.png")
print("Private Key QR Code succesfull saved as privatekey-qrcode.png")
print(spaces)
print("QR Code generate info: ", qrcode.make(addr), qrcode.make(priv))