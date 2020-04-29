import time
num = int(input('Digite um número qualquer: '))
for c in range (1,11):
    print('{} x {} = {}'.format(c, num, num*c))
    time.sleep(1)
