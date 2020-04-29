from random import randint
from time import sleep
def sorteia(lista):
    print('Sortenando os 5 números da lista: ', end='')
    for c in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
def somaPar(lista):
    soma = 0
    for c,v in enumerate(lista):
        if v % 2 == 0:
            soma += v
    print(f'\nA soma dos pares é {soma}')
daly = []
sorteia(daly)
somaPar(daly)
