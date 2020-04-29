lista = []
for c in range(1,6):
    lista.append(int(input(f'Digite o {c}º valor: ')))
print(lista)
lista.sort()
print(f'O maior valor é {lista[4]} posição {lista.index(lista[4])} e o menor é {lista[0]} posição {lista.index(lista[0])}!')