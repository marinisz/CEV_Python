import math
a = int(input('Digite o valor de uma reta: '))
b = int(input('Digite o valor de uma reta: '))
c = int(input('Digite o valor de uma reta: '))
# if a or b or c == 0:
    # break não sei usar isso
    # print('error')
if (b + c) > a and b < (a + c) and c < (c+b):
    print('Dá para fazer um triangulo!')
    if a == b and b == c:
        print('Seu triângulo é equilatero!')
    elif a != b and b != c and a != c:
        print('Seu triângulo é escaleno!')
    elif a == b or b == c or a == c:
        print('Seu triângulo é isosceles!')
else:
    print('Não dá!')
