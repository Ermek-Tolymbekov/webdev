from math import sqrt
a, b = int(input()), int(input())
for i in range(a, b + 1):
    if sqrt(i) == int(sqrt(i)):
        print(i, end=' ')
    