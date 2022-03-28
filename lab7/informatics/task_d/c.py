from calendar import c


n = int(input())
a = input().split()
cnt = int(0)
for i in range(n):
    if int(a[i]) > 0:
        cnt += 1
print(cnt)