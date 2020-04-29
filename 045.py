import random
import playsound
names = ['pedra', 'papel', 'tesoura']
computador = random.choice(names)
escolha = str(input('Digite pedra, papel ou tesoura: '))
print('\033[35m-=-\033[m'*5)
if escolha == computador:
    print('\033[33mEMPATE\033[m')
    print('Sua escolha: \033[34m{}\033[m'.format(escolha))
    print('A escolha do computador: \033[34m{}\033[m'.format(computador))
elif escolha == 'pedra' and computador == 'papel':
    print('\033[31mVITÓRIA DO COMPUTADOR\033[m')
    print('Sua escolha: \033[34m{}\033[m'.format(escolha))
    print('A escolha do computador: \033[34m{}\033[m'.format(computador))
elif escolha == 'pedra' and computador == 'tesoura':
    print('\033[34mVOCÊ VENCEU\033[m')
    print('Sua escolha: \033[34m{}\033[m'.format(escolha))
    print('A escolha do computador: \033[34m{}\033[m'.format(computador))
    playsound.playsound('patapata.mp3')
elif escolha == 'tesoura' and computador == 'pedra':
    print('\033[31mVITÓRIA DO COMPUTADOR\033[m')
    print('Sua escolha: \033[34m{}\033[m'.format(escolha))
    print('A escolha do computador: \033[34m{}\033[m'.format(computador))
elif escolha == 'tesoura' and computador == 'papel':
    print('\033[34mVOCÊ VENCEU\033[m')
    print('Sua escolha: \033[34m{}\033[m'.format(escolha))
    print('A escolha do computador: \033[34m{}\033[m'.format(computador))
    playsound.playsound('patapata.mp3')
elif escolha == 'papel' and computador == 'pedra':
    print('\033[34mVOCÊ VENCEU\033[m')
    print('Sua escolha: \033[34m{}\033[m'.format(escolha))
    print('A escolha do computador: \033[34m{}\033[m'.format(computador))
    playsound.playsound('patapata.mp3')
elif escolha == 'papel' and computador == 'tesoura':
    print('\033[31mVITÓRIA DO COMPUTADOR\033[m')
    print('Sua escolha: \033[34m{}\033[m'.format(escolha))
    print('A escolha do computador: \033[34m{}\033[m'.format(computador))
