def gcd(a, b):
    if b == 0:
        return (1, 0)
    else:
        (x, y) = gcd(b, a % b)
        return (y, x - (a // b) * y)

a = 57
b = 159
(x, y) = gcd(a, b)
print("x: " + str(x) + ", y: " + str(y) + ", gcd: " + str(x * a + y * b))
