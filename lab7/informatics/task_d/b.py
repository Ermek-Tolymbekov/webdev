n = int(input())
a = input().split()
for i in range(n):
    if not int(a[i]) % 2:
        print(a[i], end=' ')