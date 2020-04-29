par = 0
for c in range(1,7):
    num = int(input('Digite o {}º número: '))
    if num % 2 == 0:
        par += num
print('A soma dos pares = {}'.format(par))