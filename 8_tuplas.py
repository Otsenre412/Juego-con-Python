"""
ejemplos para trabajar con tuplas
"""

TUP = (1, 2, 3, 4, 5, 'seis')

print(TUP)
print(TUP[0])
print(TUP[4])
print(TUP[2:5])
print(TUP[:3])
print(TUP[2:])

print(len(TUP))

TUP += ('siete', 8, True, False)
print(TUP)

SUMA = (3 + 2) - 1
print(SUMA)

T2 = (3,) # tupla de un solo elemento, se le añade la , que sino no sabe si es un numero o una tupla
print(type(T2))