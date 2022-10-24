n = int(input())
init = input()
for i in range(n):
    arvores = dict()
    while True:
        arv = str(input())
        if arv in arvores.keys():
            arvores[arv] += 1
        else:
            arvores[arv] = 1
