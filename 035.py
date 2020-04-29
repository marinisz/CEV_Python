import math
a = int(input('Digite o valor de uma reta: '))
b = int(input('Digite o valor de uma reta: '))
c = int(input('Digite o valor de uma reta: '))
if (b + c) > a and b < (a + c) and c < (c+b):
    print('Dá para fazer um triangulo!')
else:
    print('Não dá!')