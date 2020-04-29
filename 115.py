from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['NOVO USUÁRIO', 'LISTA DE USUÁRIOS', 'SAIR DO PROGRAMA'])
    if resposta == 1:
        print('ADICIONAR NOVO USUÁRIO')
    elif resposta == 2:
        print('LISTANDO USUÁRIOS')
    elif resposta == 3:
        print('SAINDO DO PROGRAMA')
    else:
        print('\033[31mOPÇÃO INVÁLIDA\033[m')
    sleep(1.5)