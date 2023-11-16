from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from binascii import hexlify, unhexlify

# Chiave in formato esadecimale
key_hex = '1bb4545801ca1e93'
key = unhexlify(key_hex)

# Testo in chiaro
plaintext = 'La lunghezza di questa frase non è divisibile per 8'

# Applicare lo schema di riempimento x923
plaintext = pad(plaintext.encode('utf-8'), DES.block_size, style='x923')

# Generare un vettore di inizializzazione casuale
iv = get_random_bytes(DES.block_size)
# stampo Che IV hai utilizzato (in esadecimale)
print("IV: " + hexlify(iv).decode('utf-8') + "\n")

# Creare un oggetto DES in modalità CBC
cipher = DES.new(key, DES.MODE_CBC, iv)

# Cifrare il testo in chiaro
ciphertext = cipher.encrypt(plaintext)

# Stampare il testo cifrato in formato esadecimale
print("Text: " + hexlify(ciphertext).decode('utf-8') + "\n")