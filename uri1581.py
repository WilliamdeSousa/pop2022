for i in range(int(input())):
    linguas = list()
    for j in range(int(input())):
        linguas.append(input())
    if linguas.count(linguas[0]) == linguas.__len__():
        print(linguas[0])
    else:
        print('ingles')
