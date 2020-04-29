def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(msg.center(tam))
    print('~' * tam)
mens=str(input('Digite algo: '))
escreva(mens)