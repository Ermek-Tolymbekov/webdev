x = int(input())
for i in range(1, x + 1):
    if not x % i:
        print(i, end=' ')