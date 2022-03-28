n = int(input())
k = int(0)
while 2 ** k < n:
    k += 1
print(k)