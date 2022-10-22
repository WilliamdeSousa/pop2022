n_casos = int(input())
for caso in range(n_casos):
    i, f = [int(j) for j in input().split()]
    sequencia = ''.join([str(j) for j in range(i, f + 1)])
    sequencia += sequencia[::-1]
    print(sequencia)
