# n! = n*(n-1)*(n-2)...3*2*1
n = int(input('Digite um número qualquer: '))
x = 1
soma = n
y = 1
while y != 0:
    soma = soma*(n-x)
    x +=1
    y = n-x
print(soma)
