#https://learnmeabitcoin.com/guide/wif
import os, binascii, hashlib, base58, ecdsa

#priv_key = os.urandom(32)
priv_key= bytearray.fromhex('5419bda0d87d60817cac1c694c6397b51c8f4702967c24efcb4f08f31d924ae7')

def ripemd160(x):
    d = hashlib.new('ripemd160')
    d.update(x)
    return d

#80 - Mainnet
#ef - Testnet

fullkey = '80' + binascii.hexlify(priv_key).decode()
fullkey = 'ef' + binascii.hexlify(priv_key).decode()

#para chave publica comprimida adciona 01, mas tem que verficar as curvas - impar ou par para adicionar 
#fullkey = '80' + binascii.hexlify(priv_key).decode() + '01'

sha256a = hashlib.sha256(binascii.unhexlify(fullkey)).hexdigest()
sha256b = hashlib.sha256(binascii.unhexlify(sha256a)).hexdigest()

WIF = base58.b58encode(binascii.unhexlify(fullkey+sha256b[:8]))

    
# get public key , uncompressed address starts with "1"
sk = ecdsa.SigningKey.from_string(priv_key, curve=ecdsa.SECP256k1)
vk = sk.get_verifying_key()

#O resultado da final da chave pública no ECDSA é simplesmente as coordenadas da chave
#pública (32 bytes para cada uma) com um byte 0x04 como sufixo. Podemos simplesmente
#fazer algo assim:
publ_key = '04' + binascii.hexlify(vk.to_string()).decode()
hash160 = ripemd160(hashlib.sha256(binascii.unhexlify(publ_key)).digest()).digest()

publ_addr_a = b"\x00" + hash160 # P2PKH
#publ_addr_a = b"\x05" + hash160 # P2SH
#publ_addr_a = b"\x6F" + hash160 # P2PKH (testnet)
#publ_addr_a = b"\xC4" + hash160 # P2SH (testnet)

checksum = hashlib.sha256(hashlib.sha256(publ_addr_a).digest()).digest()[:4]
publ_addr_b = base58.b58encode(publ_addr_a + checksum)

#verificando os pontos x e y da curva
p = sk.get_verifying_key()

print(sk.privkey.public_key.point)
print("")
print("x: " + hex(p.pubkey.point.x()))
print("y: " + hex(p.pubkey.point.y()))
print("")
print("Private key inicial: "  + binascii.hexlify(priv_key).decode())
print("")
print("Bitcoin Address: " + publ_addr_b.decode())
print("")
print('Public Key (130 characters [0-9A-F]):' + publ_key)
print("")
print("Private Key WIF: " + WIF.decode())





