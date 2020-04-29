import random
import playsound

names = ['pedra', 'papel', 'tesoura']
computador = random.choice(names)
escolha = str(input('Digite pedra, papel ou tesoura: '))
print('\033[35m-=-\033[m'*5)
if escolha == 'pedra' and computador == 'papel' or escolha == 'tesoura' and computador == 'pedra' or escolha == 'papel' and computador == 'tesoura':
    print('\033[31mVITÓRIA DO COMPUTADOR\033[m')
    print('Sua escolha: \033[35m{}\033[m'.format(escolha))
    print('A escolha do computador: \033[35m{}\033[m'.format(computador))
elif escolha == 'papel' and computador == 'pedra' or escolha == 'tesoura' and computador == 'papel' or escolha == 'pedra' and computador == 'tesoura':
    print('\033[34mVOCÊ VENCEU\033[m')
    print('Sua escolha: \033[35m{}\033[m'.format(escolha))
    print('A escolha do computador: \033[35m{}\033[m'.format(computador))
    playsound.playsound('patapata.mp3')