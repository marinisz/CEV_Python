a = ('Pão', 1.00, 'Caderno', 2.59, 'Sabonete', 5.33, 'Abacate', 10.00, 'Elefante', 55.22, 'Cachorro', 9.99)
print('\033[34m-'*30)
print('      LISTAGEM DE PREÇOS')
print('-'*30)
for pos in range(0,len(a)):
    if pos % 2 == 0:
        print(f'{a[pos]:.<30}', end='')
    else:
        print(f'R${a[pos]:>6.2f}')
print('-'*38)