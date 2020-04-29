def vote(ano):
    s = 2019 - ano
    if 18 <= s <= 65:
        print('VOTO OBRIGATORIO')
    elif s < 16:
        print('VOTO NEGADO')
    else:
        print('VOTO OPCIONAL')


vote(int(input('Digite seu ano de nascimento: ')))
