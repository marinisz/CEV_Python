import math
n = int(input('Digite o cateto adjacente do triangulo: '))
x = int(input('Digite o cateto oposto do triangulo: '))
print('A hipotenusa do triangulo inserido de catetos {} e {} é {}'.format(n,x,math.sqrt((math.pow(n,2)+math.pow(x,2)))))