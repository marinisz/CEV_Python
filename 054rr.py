maior = 0
menor = 0
for c in range(1,8):
    print('===={}ª PESSOA===='.format(c))
    ano = int(input('Qual o ano de seu nascimento? -> '))
    if ano < 2001:
        maior += 1
    else:
        menor += 1
print('De maior = {}.De menor = {}.'.format(maior,menor))