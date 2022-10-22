n_casos = int(input())
for c in range(n_casos):
    matricula = str(input())
    if matricula.startswith('RA') and len(matricula) == 20:
        print(int(matricula[2:]))
    else:
        print('INVALID DATA')
