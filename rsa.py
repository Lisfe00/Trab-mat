from Crypto.PublicKey import RSA
   2 from Crypto.Util.randpool import RandomPool
   3 
   4 texto = "texto a encriptar"
   5 
   6 # Você deve usar a melhor fonte de dados aleatórios que tiver à
   7 # disposição. Pra manter o exemplo mais portável, usaremos o
   8 # RandomPool do próprio PyCrypto:
   9 
  10 pool = RandomPool(384)
  11 pool.stir()
  12 
  13 # randfunc(n) deve retornar uma string de dados aleatórios de
  14 # comprimento n, no caso de RandomPool, o método get_bytes
  15 randfunc = pool.get_bytes
  16 
  17 # Se tiver uma fonte segura (como /dev/urandom em sistemas unix), ela
  18 # deve ser usada ao invés de RandomPool
  19 
  20 # pool = open("/dev/urandom")
  21 # randfunc = pool.read
  22 
  23 # Tamanho da chave, em bits
  24 N = 256
  25 
  26 # O algoritmo RSA usado aqui não utiliza K, que pode ser uma string
  27 # nula.
  28 K = ""
  29 
  30 # Geramos a chave (contendo a chave pública e privada):
  31 key = RSA.generate(N, randfunc)
  32 
  33 # Criptografamos o texto com a chave:
  34 enc = key.encrypt(texto, K)
  35 
  36 # Podemos decriptografar usando a chave:
  37 dec = key.decrypt(enc)
  38 
  39 # Separando apenas a chave pública:
  40 pub_key = key.publickey()
  41 
  42 # Criptografando com a chave pública:
  43 enc = pub_key.encrypt(texto, K)
  44 
  45 # Decriptografando com a chave privada:
  46 dec = key.decrypt(enc)
  47 
  48 # As informações da chave são compostas de seis atributos: 'n', 'e',
  49 # 'd', 'p', 'q' e 'u'. Se quiser armazenar ou enviar uma chave você
  50 # pode usar pickle ou simplesmente usar esses atributos com o método
  51 # construct. Por exemplo:
  52 
  53 # Os atributos 'n' e 'e' correspondem à chave pública:
  54 n, e = key.n, key.e
  55 
  56 # E recriamos a chave pública com esses dados:
  57 pub_key = RSA.construct((n, e))