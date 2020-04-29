n = str(input('Digite uma frase qualquer: ')).strip().upper()
print('A letra a aparece {} vezes nessa frase!'.format(n.count('A')))
print('A letra a aparece primeiro na {} posição'.format(n.find('A')+1))
print('A letra a aparece por ultimo na {} posição'.format(n.rfind('A')+1))