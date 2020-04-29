import random
a = str(input('Nome do primeiro aluno: '))
b = str(input('Nome do segundo aluno: '))
c = str(input('Nome do terceiro aluno: '))
d = str(input('Nome do quarto aluno: '))
ids = a,b,c,d
print('O aluno escolhido é {}'.format(random.choice(ids)))
