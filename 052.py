tot=0
num = int(input('Digite um número qualquer: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
if tot == 2:
    print('\n\033[36mÉ UM NÚMERO PRIMO!!!!')
else:
    print('\n\033[36NÃO É UM NÚMERO PRIMO')