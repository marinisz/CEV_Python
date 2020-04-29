n1 = int(input('Digite um número de 1 à 9: '))
n2 = int(input('Digite outro número de 1 à 9: '))
n3 = int(input('Digite mais um número de 1 à 9: '))
if n1<n2<n3:
    print('{} é o maior número seguido de {} e {}!'.format(n3,n2,n1))
if n1<n3<n2:
    print('{} é o maior número seguido de {} e {}!'.format(n2, n3, n1))
if n2<n1<n3:
    print('{} é o maior número seguido de {} e {}!'.format(n3, n1, n2))
if n2<n3<n1:
    print('{} é o maior número seguido de {} e {}!'.format(n1, n3, n2))
if n3<n2<n1:
    print('{} é o maior número seguido de {} e {}!'.format(n1, n2, n3))
if n3<n1<n2:
    print('{} é o maior número seguido de {} e {}!'.format(n2, n1, n3))
