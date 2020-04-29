import time
n1 = int(input('\033[34mDigite um número inteiro: \033[m'))
time.sleep(0.2)
n2 = int(input('\033[34mDigite outro número: \033[m'))
time.sleep(0.5)
print('-------------------------------------------------------------')
time.sleep(0.2)
x = 0
while x != 5:
    time.sleep(1.5)
    print('\033[34mO que deseja fazer com esses números:\033[m')
    time.sleep(0.4)
    print('[1] SOMAR')
    time.sleep(0.4)
    print('[2] MULTIPLICAR')
    time.sleep(0.4)
    print('[3] MOSTRAR O MAIOR')
    time.sleep(0.4)
    print('[4] DIGITAR MAIS NÚMEROS')
    time.sleep(0.4)
    print('[5] SAIR DO PROGRAMA')
    time.sleep(0.4)
    x = int(input('\033[34m>>>>>>Meu desejo é: \033[m'))
    if x == 1:
        print('A soma é = {}.'.format(n1+n2))
    elif x == 2:
        print('A multiplicação é = {}.'.format(n1*n2))
    elif x == 3:
        if n1 > n2:
            print('{} é maior que {}.'.format(n1,n2))
        else:
            print('{} é maior que {}.'.format(n2, n1))
    elif x == 4:
        print('--Informe seus novos valores--')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif x == 5:
        print('\033[31mFIM DO PROGRAMA\033[m')
    else:
        print('Opção invalida!')
