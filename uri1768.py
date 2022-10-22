while True:
    try:
        num = int(input())
    except EOFError:
        break
    folhas = 1
    num_espacos = (num - 1) // 2
    while folhas <= num:
        print(f'{" " * num_espacos}{"*" * folhas}')
        folhas += 2
        num_espacos -= 1
    num_espacos = (num - 1) // 2
    print(f'{" " * num_espacos}*')
    num_espacos -= 1
    print(f'{" " * num_espacos}***')
    print()
