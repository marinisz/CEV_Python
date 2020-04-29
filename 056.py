totidade = 0
velho = ''
velhoidade = 0
mulher20 = 0
for c in range (1,5):
    print('-----{}ª PESSOA-----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    totidade += idade
    if c == 1 and sexo == 'M':
        velhoidade = idade
        velho = nome
    if sexo == 'M' and idade > velhoidade:
        velhoidade = idade
        velho = nome
    if sexo == 'F' and idade < 20:
        mulher20 += 1

midade = totidade/4
print('A média das idades é {} anos'.format(midade))
print('O homem mais velho é o {}'.format(velho))
print('{} mulheres tem menos de 20 anos'.format(mulher20))