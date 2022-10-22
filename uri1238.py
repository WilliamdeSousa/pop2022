for i in range(int(input())):
    a, b = input().split()
    c = list()
    for letra in range(min([len(a), len(b)])):
        c.append(a[letra])
        c.append(b[letra])
    if len(a) != len(b):
        if len(b) < len(a):
            c.append(a[min([len(a), len(b)]):])
        else:
            c.append(b[min([len(a), len(b)]):])
    print(''.join(c))
