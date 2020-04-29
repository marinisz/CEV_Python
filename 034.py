cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'ciano':'\033[36m',
         'pretoebranco':'\033[7;30m'}

s = int(input('Qual o seu salário? (digite aqui)->'))
if s>1250:
    print('Parabéns, seu novo salário é: {}{}{}!'.format(cores['azul'], s+(s*0.1), cores['limpa']))
else:
    print('Parabéns, seu novo salário é: {}{}{}!'.format(cores['vermelho'], s+(s*0.15), cores['limpa']))