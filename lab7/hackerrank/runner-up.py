if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    sec = -101
    fir = max(arr)
    for i in arr:
        if i > sec and i < fir:
            sec = i
    print(sec)
