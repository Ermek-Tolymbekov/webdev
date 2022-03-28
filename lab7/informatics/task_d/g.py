n = int(input())
a = input().split()
for i in range(int(n / 2)):
    b = a[i]
    a[i] = a[n - i - 1]
    a[n - i - 1] = b
for i in a:
    print(i, end=' ')