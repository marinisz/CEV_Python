pesao = 0
pesinho = 0
pesado = ''
pesadinho = ''
for c in range(1,4):
    print('===={}ª PESSOA===='.format(c))
    nome = str(input('NOME: '))
    peso = float(input('PESO: '))
    if c == 1:
        pesao = peso
        pesado = nome
        pesinho = peso
        pesadinho = nome
    else:
        if peso > pesao:
            pesao = peso
            pesado = nome
        if peso < pesinho:
            pesinho = peso
            pesadinho = nome
print('O pesadão é o {} e o levinho é o {}.'.format(pesado,pesadinho))
