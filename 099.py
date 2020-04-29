import time
def maior(*num):
    cont = maioral =  0
    time.sleep(0.2)
    print('\n\033[34mAnalisando os valores passados...\033[m')
    for valor in num:
        print(f'{valor} ',end='', flush=True)
        time.sleep(0.35)
        if cont == 0:
            maioral = valor
        else:
            if valor > maioral:
                maioral = valor
    cont += 1
    time.sleep(0.2)
    print(f'\nO maior valor é: {maioral}')
maior(1,2,3,5)
maior(4,7,9)
maior(1,2)
maior(1)
maior()