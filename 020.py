import random
pri = str(input('Nome do primeiro grupo: '))
seg = str(input('Nome do segundo grupo: '))
ter = str(input('Nome do terceiro grupo: '))
qua = str(input('Nome do quarto grupo: '))
nomes = [pri, seg, ter, qua]
random.shuffle(nomes)
print('A ordem de apresentação é ')
print(nomes)