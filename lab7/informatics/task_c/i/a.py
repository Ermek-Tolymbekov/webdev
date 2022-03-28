a, b = int(input()), int(input())
for i in range(a, b + 1):
    if not i % 2:
        print(i, end=' ')