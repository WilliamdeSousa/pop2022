valor = float(input()) * 100
print('NOTAS:')
for nota in [10000, 5000, 2000, 1000, 500, 200]:
    print(f'{valor // nota:.0f} nota(s) de R$ {nota / 100:.2f}')
    valor -= (valor // nota) * nota
print('MOEDAS:')
for moeda in (100, 50, 25, 10, 5, 1):
    print(f'{valor // moeda:.0f} moeda(s) de R$ {moeda / 100:.2f}')
    valor -= (valor // moeda) * moeda
