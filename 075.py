n = (int(input('Digite um valor de 1 à 9: ')), int(input('Outro valor: ')), int(input('Mais um valor: ')), int(input('O último valor: ')))
x = n.count(9)
print(n)
print(f'O 9 aparece {x} vezes.')
if 3 in n:
    print(f'O 3 aparece {n.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado!')
print('Os números pares são: ', end='')
for c in n:
    if c % 2 ==0:
        print(c, end=' ')

