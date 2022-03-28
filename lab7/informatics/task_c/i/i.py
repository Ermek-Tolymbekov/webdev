import math
x = int(input())
n = int(0)
j = int(math.sqrt(x))
for i in range(1, j + 1):
    if i * i == x:
        n += 1
    elif not x % i:
        n += 2
    
print(n)