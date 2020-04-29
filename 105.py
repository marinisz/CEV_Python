def notas(*n, sit=False):
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] <= 5:
            r['Situação'] = 'Insuficiente'
        if 5 < r['Média'] < 7:
            r['Situação'] = 'Boa'
        if r['Média'] > 7:
            r['Situação'] = 'Ótima'
    return r


# programa_principal:
resp = (notas(8, 5, 4.5, 10, sit=True))
print(resp)
