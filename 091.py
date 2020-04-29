from random import randint
from time import sleep
from operator import itemgetter
jogo = {'1': randint(1,6), '2': randint(1,6), '3': randint(1,6), '4': randint(1,6)}
ranking = {}
for k, v in jogo.items():
    print(f'O {k}º jogador tirou: {v}')
    sleep(0.6)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'Em {i+1}º Lugar - Jogador {v[0]} tirou {v[1]}')
    sleep(0.5)













# jogo1 = {'nome': 'player1', 'número': randint(0, 9)}
# jogo2 = {'nome': 'player2', 'número': randint(0, 9)}
# jogo3 = {'nome': 'player3', 'número': randint(0, 9)}
# jogo4 = {'nome': 'player4', 'número': randint(0, 9)}



