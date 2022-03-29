if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    fl = float(100)
    sl = float(100)
    for i in students:
        if i[1] < fl:
            fl = i[1]
    for i in students:
        if i[1] < sl and fl < i[1]:
            sl = i[1]
    res = []
    for i in students:
        if i[1] == sl:
            res.append(i[0])
    res.sort()
    for i in res:
        print(i)