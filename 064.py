num = 0
tentativas = 0
soma = 0
while num != 999:
    num = int(input('Digite um número entre 0 e 1200: '))
    tentativas += 1
    soma = soma + num
print('Finalmente acabamos, você fez {} tentativas e a soma deu {}!'.format(tentativas,soma))