while True:
    try:
        n_casos = int(input())
    except EOFError:
        break
    codigos = list()
    for c in range(n_casos):
        codigos.append(str(input()))
    codigos_ordenados = sorted(codigos)
    for c in codigos_ordenados:
        print(c)