def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mDIGITOU UM NÃO INTEIRO\033[m')
            continue
        except KeyboardInterrupt:
            print('ARREGOU')
            return 0

        else:
            return n


n = leiaint('Digite um valor: ')
print(f'\033[34mSeu número é {n}\033[m')