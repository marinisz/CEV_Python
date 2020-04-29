jogador = dict()
jogador['PARTIDAS JOGADAS'] = int(input('PARTIDAS JOGADAS: '))
for c in range (1,jogador['PARTIDAS JOGADAS']+1):
    jogador[f'GOL NA {c}ª PARTIDA'] = int(input(f'Gols na {c}ª partida: '))
soma = 0
for c in range (1,jogador['PARTIDAS JOGADAS']+1):
    soma = soma + jogador[f'GOL NA {c}ª PARTIDA']
jogadas = jogador['PARTIDAS JOGADAS']
for k,v in jogador.items():
    print(f'{k} - {v}')
print(f'{soma} = total de gols')