import playsound
import random
n = random.randint(1,10)
tentativas = 0
soma = 0
print('\033[34m-----==* ESTOU PENSANDO EM UM NÚMERO DE 0 À 10 *==-----\033[m')
valor = int(input('Digite seu palpite: '))
while valor != n:
    valor = int(input('Tente novamente: '))
    tentativas += 1
    soma += valor
print('Você acertou, eu pensei mesmo no {}. Mas para tanto você teve {} tentativas e a soma dos chutes é {}.'.format(n,tentativas,soma))
playsound.playsound('acertou.mp3')