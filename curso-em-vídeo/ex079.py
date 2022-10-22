lista = list()
while True:
    num = float(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
    if str(input('Quer continuar? [S/N] '))[0].upper() == 'N':
        break
print(f'Os valores digitados foram: {lista}')
