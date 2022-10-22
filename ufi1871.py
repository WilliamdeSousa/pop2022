caso = input()
while caso != '0 0':
    print(str(sum([int(i) for i in caso.split()])).replace('0', ''))
    caso = input()
