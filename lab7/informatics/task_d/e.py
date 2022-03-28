n = int(input())
a = input().split()
a = [int(i) for i in a]
b = bool(0)
for i in range(1, n):
    if a[i] > 0 and a[i-1] > 0 or a[i] < 0 and a[i-1] < 0:
        b = True
print('YES' if b else 'NO')