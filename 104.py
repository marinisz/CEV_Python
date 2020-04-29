def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            print(f'\033[34mÉ um número -> {n}\033[m')
            ok = True
        else:
            print('\033[31mNÃO É UM NÚMERO\033[m')
        if ok:
            break
    return valor

n = leiaint('Digite um valor: ')