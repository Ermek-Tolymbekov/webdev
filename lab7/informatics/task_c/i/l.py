x = input()
j = int(0)
num = int(0)
for i in range(len(x) - 1, -1, -1):
    num += int(x[i]) * 2 ** j
    j += 1
print(num)