from time import sleep

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'ciano':'\033[36m',
         'pretoebranco':'\033[7;30m'}

def ajuda(msg):

    """Digite qualquer comando ou biblioteca e te mostrarei o que ele faz!"""

    titulo('Acessando o manual do comando','verde')
    sleep(1.5)
    print(cores['ciano'])
    help(msg)
    print(cores['limpa'])
    sleep(1.5)
def titulo(msg, cor='limpa'):
    tam = len(msg)
    print(cores[cor], end='')
    print('~'*(tam+4))
    print(f'  {msg}  ')
    print('~'*(tam+4))
    print(cores['limpa'], end='')


# programa principal:
titulo('BEM VINDO CACETA','azul')
sleep(0.5)
while True:
    comando = str(input('Comando ou Biblioteca: '))
    sleep(0.5)
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('VALEU PORRA','vermelho')