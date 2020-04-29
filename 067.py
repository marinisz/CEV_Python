import time
n = 0
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    for c in range(1,11):
        print(f'{c}x{n}= {c*n}')
        time.sleep(0.3)
print('Fim')

