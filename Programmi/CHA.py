from Crypto.Cipher import ChaCha20
from binascii import unhexlify

# Chiave in formato esadecimale
key_hex = '9d6a8f22e962f16259e46292bea8a7b2a886785bee9007ac887cd2a5fe476e49'
key = unhexlify(key_hex)

# Testo cifrato in formato esadecimale
ciphertext_hex = 'b7e9ac65d85c41c065c8af15c0ea2eca8f6e73b18ff7c3a8f78abf74'
ciphertext = unhexlify(ciphertext_hex)

# Nonce in formato esadecimale
nonce_hex = '76c24201d182bab1'
nonce = unhexlify(nonce_hex)

# Creare un oggetto ChaCha20
cipher = ChaCha20.new(key=key, nonce=nonce)

# Decifrare il testo cifrato
plaintext = cipher.decrypt(ciphertext)

# Stampa il testo in chiaro
print(plaintext.decode('utf-8'))