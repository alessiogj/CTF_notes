from Crypto.Hash import SHA256

from binascii import hexlify

# Testo in chiaro
plaintext = 'La lunghezza di questa frase non e divisibile per 8'

# Creare un oggetto SHA256
h = SHA256.new()

# Aggiornare l'hash con il testo in chiaro
h.update(plaintext.encode('utf-8'))

# Calcolare l'hash
digest = h.digest()

# Stampa l'hash in formato esadecimale
print(hexlify(digest).decode('utf-8'))