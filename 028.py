import random
import playsound
a=(random.randint(1,5))
x=int(input('Colé menor, pensei num númiru de 1 a 5, chuta ai: '))
if x == a:
    print('Deitou em mermão!')
    print('Eu pensei no {} mesmo!'.format(a))
    playsound.playsound('timmaialofi.mp3')
else:
    print('errou rude')
    print('Eu pensei no {}'.format(a))
