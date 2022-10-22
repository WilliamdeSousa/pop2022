pares = list()
impares = list()
for i in range(15):
    n = int(input())
    if n % 2 == 1:
        impares.append(n)
        print(f'impar[{len(impares) - 1}] = {n}')
    elif n % 2 == 0:
        pares.append(n)
        print(f'par[{len(pares) - 1}] = {n}')
    if len(pares) == 5:
        pares.clear()
    if len(impares) == 5:
        impares.clear()
q_par = len(pares)
q_impar = len(impares)
for i in range(q_par):
    print(f'par[{i}] = {pares[i]}')
for i in range(q_impar):
    print(f'impar[{i}] = {impares[i]}')