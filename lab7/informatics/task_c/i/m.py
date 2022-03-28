n = int(input())
zeros = int(0)

for i in range(n):
    zeros += not int(input())

print(zeros)