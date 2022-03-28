n = int(input())
a = input().split()
a = [int(i) for i in a]
cnt = int(0)
for i in range(1, n - 1):
    if a[i] > a[i-1] and a[i] > a[i+1]:
        cnt += 1
print(cnt)