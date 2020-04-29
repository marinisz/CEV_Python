mdia = 0
n = 0
resp = ''
soma = 0
tent = 0
menor = 999999999
while resp != 'N':
    n = int(input('Digite um número inteiro: '))
    tent += 1
    soma = soma + n
    mdia = soma/tent
    if n < menor:
        menor = n
    resp = str(input('\033[34mVocê quer continuar [s/n]:\033[m')).upper()[0].strip()
print('A média entre seus números é {}  e o menor é {}.'.format(round(mdia),menor))
