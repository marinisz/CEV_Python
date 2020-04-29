cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'vermelho':'\033[31m'}
x = int(input('Qual a distância até seu detino? '))
if x <=200:
    print('O valor da passagem é {}{}{} reais'.format(cores['azul'],int(x*0.5),cores['limpa']))
else:
    print('O valor da passagem é {}{}{} reais'.format(cores['vermelho'],int(x*0.45),cores['limpa']))