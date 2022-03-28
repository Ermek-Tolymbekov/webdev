a = int(input())
i = int(2)
while i <= a:
    if not a % i:
        print(i)
        break
    i += 1