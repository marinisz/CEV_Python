from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1,8):
    nasc = float(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Ao todo tivemos: {} pessoas maiores e {} pessoas menores!'.format(totalmaior,totalmenor))