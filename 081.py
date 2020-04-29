quant = 0
maior = 0
lista = []
resp = ''
while True:
    n = int(input('Digite um número: '))
    quant += 1
    lista.append(n)
    resp = str(input('[S/N] >>>')).upper().strip()
    if resp == 'N':
        break
lista.sort()
lista.sort(reverse=True)
print(f'A lista tem {quant} elementos')
print('=*='*30)
print(f'A lista em ordem decrescente é {lista}')
print('=*='*30)
if 5 in lista:
    print('O 5 aparece!')
