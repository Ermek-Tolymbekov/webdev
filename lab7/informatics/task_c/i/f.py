x = input()
rev = int(0)
for i in range(len(x) - 1, -1, -1):
    rev *= 10
    rev += int(x[i])
print(rev)