"""
generando numeros aleatorios
"""

import random

for n in range(10):
    print('entero aleatorio:', random.randint(10, 20))

# numeros aleatorios entre 0 y 1

for n in range(4):
    print(random.random())

# elemento aleatorio de una lista

L = ['oscar', 'lucia', 'jaime', 'pepe', 'cris', 'yolanda', 'sara']

for n in range(8):
    print(random.choice(L))

# elementos aleatorios de una lista (pueden llegar repetidos)

r = random.choices(L, k=3) # k es el numero de elementos que queremos

print('==========')    # separador
print(r)

# cambiar orden de eleemtnos de una lista de forma aleatoria

random.shuffle(L)
print(L)

# a partir de una lista, crear otra con k elementos que no esten repetidos

print('==========')
print(random.sample(L, k=2))
print(random.sample(L, k=2))
print(random.sample(L, k=2))
print(random.sample(L, k=2))
print(random.sample(L, k=2))
print(random.sample(L, k=2))
print(random.sample(L, k=2))
print(random.sample(L, k=2))
print(random.sample(L, k=2))