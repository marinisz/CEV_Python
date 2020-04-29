from abacaxi import moeda
from time import sleep
p = float(input('Digite um valor: '))
sleep(1)
print(f'O dobro de {moeda.formata(p,True)} é {moeda.dobro(p,True)}')
sleep(1)
print(f'A metade de {moeda.formata(p,True)} é {moeda.metade(p,True)}')
sleep(1)
print(f'Aumentando 10% em {moeda.formata(p,True)} temos {moeda.aumenta(p,10,True)}')
sleep(1)
print(f'Diminuindo 20% em {moeda.formata(p,True)} temos {moeda.diminua(p,20,True)}')
sleep(1)
print(moeda.formata(p,True))