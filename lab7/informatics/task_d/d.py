n = int(input())
a = input().split()
cnt = int(0)
for i in range(1, n):
    if(int(a[i]) > int(a[i - 1])):
        cnt += 1
print(cnt)