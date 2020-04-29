import random
import time
resultado = ''
vit = 0
jogada = 0
desejo = ''
pc = 0
print('\033[36mVAMOS JOGAR PAR OU IMPAR!!!!!!\033[m')
time.sleep(0.5)
while True:
    pc = random.randint(0,10)
    jogada = int(input('Digite seu número: '))
    desejo = str(input('Par ou impar? [P/I] ->>')).upper().strip()
    if (jogada + pc) %2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    if desejo == resultado:
        print('VOCÊ VENCEU!')
        vit += 1
    else:
        print('VOCÊ PERDEU!')
        break
print(f'\033[34mVocê venceu {vit} vez(es) campeão!\033[31m')