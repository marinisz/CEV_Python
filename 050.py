soma = 0
for c in range(1,7):
    x = int(input('Digite o {} número: '.format(c)))
    if x % 2 == 0:
        soma += x
print ('A soma dos números pares é: {}!'.format(soma))

