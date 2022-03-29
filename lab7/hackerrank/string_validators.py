if __name__ == '__main__':
    s = input()
    alphanum = bool(False)
    alphab = bool(False)
    digits = bool(False)
    lowcase = bool(False)
    upcase = bool(False)
    for i in s:
        if i.isalnum():
            alphanum = True
        if i.isalpha():
            alphab = True
        if i.isdigit():
            digits = True
        if i.islower():
            lowcase = True
        if i.isupper():
            upcase = True
    print(alphanum, alphab, digits, lowcase, upcase, sep='\n')
    