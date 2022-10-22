for caso in range(int(input())):
    a, b = [str(i) for i in input().split()]
    if a.endswith(b):
        print('encaixa')
    else:
        print('nao encaixa')
