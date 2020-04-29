cont = str(input('Digite sua expressão: '))
x = cont.count('(')
z = cont.count(')')
if x == z:
    print('Esta ok')
else:
    print('Tá errado')
