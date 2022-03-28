n = int(input())
deg = bool(1)

while n > 1:
    if n % 2:
        deg = False
    n = (int) (n / 2)
print('YES' if deg else 'NO')