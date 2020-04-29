from datetime import datetime
dados = {}
dados['NOME'] = str(input('NOME: ')).upper()
nascimento = int(input('ANO DE NASCIMENTO: '))
dados['IDADE'] = datetime.now().year - nascimento
dados['CTPS'] = int(input('CTPS (0 = NÃO TEM) : '))
if dados['CTPS'] !=0 :
    dados['ANO DE CONTRATAÇÃO'] = int(input('ANO DE CONTRATAÇÃO: '))
    dados['SALÁRIO'] = int(input('SALÁRIO: '))
    dados['APOSENTADORIA'] = dados['IDADE'] + (dados['ANO DE CONTRATAÇÃO'] + 35) - datetime.now().year
for k, v in dados.items():
    print(f'{k} ----- {v}')