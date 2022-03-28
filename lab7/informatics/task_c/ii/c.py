a = int(input())
i = int(1)
print(i, end=' ')
while i <= a:
    if not i % 2:
        print(i, end=' ')
    i *= 2