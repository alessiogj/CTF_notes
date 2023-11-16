from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from binascii import hexlify, unhexlify

# Generare una chiave casuale AES256 in formato esadecimale
key = get_random_bytes(32)  # 32 byte per AES256

# Testo in chiaro
plaintext = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'

# Applicare lo schema di riempimento PKCS7
plaintext = pad(plaintext.encode('utf-8'), AES.block_size)

# Generare un vettore di inizializzazione casuale
iv = get_random_bytes(AES.block_size)
# Stampo che IV hai utilizzato (in esadecimale)
print("IV:", hexlify(iv).decode('utf-8'))

# Creare un oggetto AES in modalità CFB con segment size di 24
cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=24)

# Cifrare il testo in chiaro
ciphertext = cipher.encrypt(plaintext)

# Stampare la chiave in formato esadecimale
print("Chiave:", hexlify(key).decode('utf-8'))

# Stampare il testo cifrato in formato esadecimale
print("Testo cifrato:", hexlify(ciphertext).decode('utf-8'))