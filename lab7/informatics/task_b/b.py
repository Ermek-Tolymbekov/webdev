y = int(input())
if (not y % 4 and y % 100) or not y % 400:
    print('YES')
else:
    print('NO')
