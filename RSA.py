
from Crypto.PublicKey import RSA
from Crypto.Util.randpool import RandomPool 
texto = "texto a encriptar"
pool = RandomPool(38)
pool.stir()
randfunc = pool.get_bytes
N = 64
K = ""
key = RSA.generate(N, randfunc)
enc = key.encrypt(texto, K)
dec = key.decrypt(enc)
pub_key = key.publickey()
enc = pub_key.encrypt(texto, K)
dec = key.decrypt(enc)
n, e = key.n, key.e
pub_key = RSA.construct((n, e))

print('Chave:', key)
print('Encriptada:', enc)
print('Decriptada:', dec)
