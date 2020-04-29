import random
n = (random.randint(0,999), random.randint(0,999), random.randint(0,999), random.randint(0,999), random.randint(0,999))
x = sorted(n)
print(n)
print(f'O menor número é o {x[0]}')
print(f'O maior número é o {x[4]}')
