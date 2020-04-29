jogador = dict()
time = list()
while True:
    jogador.clear()
    jogador['NOME'] = str(input('NOME: '))
    jogador['PARTIDAS JOGADAS'] = int(input('PARTIDAS JOGADAS: '))
    for c in range (1,jogador['PARTIDAS JOGADAS']+1):
        jogador[f'GOL NA {c}ª PARTIDA'] = int(input(f'Gols na {c}ª partida: '))
    soma = 0
    for c in range (1,jogador['PARTIDAS JOGADAS']+1):
        soma = soma + jogador[f'GOL NA {c}ª PARTIDA']
    jogadas = jogador['PARTIDAS JOGADAS']
    time.append(jogador.copy())
    while True:
        resp = str(input('Continuar [S/N]: ')).upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break
for k,v in jogador.items():
    print(f'{k} - {v}')
print(f'{soma} = total de gols')
print('=-'*30)