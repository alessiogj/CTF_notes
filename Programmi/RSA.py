p = 36652254321470221037
q = 31629674241453983353
e = 65537
n = p * q 
phi = (p - 1) * (q - 1)
d = pow (e, -1, phi)
print("n = ", n)

print("phi(n) = ", phi)

print("d = ", d)

stringa = "Stringa di prova"

numero = int(''.join(format(ord(char), '08b') for char in stringa), 2)

cifrato = pow(numero, d, n)

print("La stringa cifrata è: ", cifrato)

