alunos = []
tudo = []
while True:
    nome = str(input('NOME: '))
    nota1 = int(input('NOTA 1:'))
    nota2 = int(input('NOTA 2:'))
    media = (nota1 + nota2) / 2
    alunos.append(nome)
    alunos.append(nota1)
    alunos.append(nota2)
    alunos.append(media)
    tudo.append(alunos[:])
    alunos.clear()
    resp = str(input('ADICIONAR ALUNO: [S/N] >>>>>')).upper().strip()
    if resp == 'N':
        break
print(tudo)
print('-='*30)
print('Nº---NOME---MÉDIA')
while True:
    for c in range(0,len(tudo)):
        print(f'|{c:<0}|  |{tudo[c][0]:^4}|  |{tudo[c][3]:4}|')
    for c in range(0,len(tudo)):
        perg = int(input('Deseja ver as notas de algum aluno? Digite seu número ou 80 para sair: '))
        if perg == c:
            print(f'Primeira nota:{tudo[c][1]} - Segunda nota:{tudo[c][2]}')
    if perg == 80:
        break
