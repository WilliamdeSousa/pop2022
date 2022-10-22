numeros = [int(input()) for i in range(5)]
print(max(numeros), end=' ')
for i in range(5):
    if numeros[i] == max(numeros):
        print(i + 1, end=' ')
print()
print(min(numeros), end=' ')
for i in range(5):
    if numeros[i] == min(numeros):
        print(i + 1, end=' ')
print()
