l = input().split()
a, b, c, d = int(l[0]), int(l[1]), int(l[2]), int(l[3])
def min(a, b, c, d):
    m1 = a if a < b else b
    m2 = c if c < d else d
    return m1 if m1 < m2 else m2
print(min(a,b,c,d))
