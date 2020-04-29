lista1 = []
lista2 = []
lista3 = []
pares = []
for c in range (1,4):
    lista1.append(int(input(f'Digite o {c}º valor: ')))
for b in range (4,7):
    lista2.append(int(input(f'Digite o {b}º valor: ')))
for a in range (7,10):
    lista3.append(int(input(f'Digite o {a}º valor: ')))
print(f'[ {lista1[0]:^5} ]', end='')
print(f'[ {lista1[1]:^5} ]', end='')
print(f'[ {lista1[2]:^5} ]\n', end='')
print(f'[ {lista2[0]:^5} ]', end='')
print(f'[ {lista2[1]:^5} ]', end='')
print(f'[ {lista2[2]:^5} ]\n', end='')
print(f'[ {lista3[0]:^5} ]', end='')
print(f'[ {lista3[1]:^5} ]', end='')
print(f'[ {lista3[2]:^5} ]',)
for c in range (0,3):
    if lista1[c]%2==0:
        pares.append(lista1[c])
for c in range (0,3):
    if lista2[c]%2==0:
        pares.append(lista2[c])
for c in range (0,3):
    if lista3[c]%2==0:
        pares.append(lista3[c])
soma = 0
print(pares)
for c in range(0,(len(pares))):
    soma = soma + (pares[c])
print(f'A soma dos pares é {soma}')
print(f'A soma da 3ª coluna é {(lista1[2]) + (lista2[2]) + (lista3[2])}')
lista2.sort()
print(f'O maior da Segunda Linha é {lista2[2]}')