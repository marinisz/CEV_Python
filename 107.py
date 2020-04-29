from abacaxi import moeda
from time import sleep
p = float(input('Digite um valor: '))
sleep(1)
print(f'O dobro de {p} é {moeda.dobro(p)}')
sleep(1)
print(f'A metade de {p} é {moeda.metade(p)}')
sleep(1)
print(f' Aumentando 10% em {p} temos {moeda.aumenta(p,10)}')
sleep(1)
print(f' Diminuindo 20% em {p} temos {moeda.diminua(p,20)}')