n = 9999999999999
tent = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s+n
    tent += 1
print(f'Você tentou {tent} vezes e a soma delas é {s}')
