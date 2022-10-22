criancas = list()
while True:
    try:
        criancas.append(str(input()))
    except EOFError:
        break
ultima = sorted([crianca.upper() for crianca in criancas], reverse=True)[0]
for crianca in criancas:
    if crianca.upper() == ultima:
        print(crianca)
