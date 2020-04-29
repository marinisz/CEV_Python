def ficha(nome='<desconhecido>', gol=0):
    """Você deve colocar o nome do
    jogador e após os gols marcados"""
    print(f'NOME:{nome}')
    print(f'GOLS FEITOS: {gol}')


n = str(input('NOME: '))
g = str(input('GOLS MARCADOS: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)