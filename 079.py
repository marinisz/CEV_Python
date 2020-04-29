lista = []
resp = ''
while resp != 'N':
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    resp = str(input('Continuar? [S/N] >>')).upper().strip()
print(lista)
lista.sort()
print(lista)