"""
ejemplos para trabajar con listas
"""

LIST = [1, 2, 3, 4, 5, 'seis', 'siete']

print(LIST)
print(LIST[0])
print(LIST[4])
print(LIST[2:5])
print(LIST[:3])
print(LIST[2:])

SIZE = len(LIST)
print('Tamaño de la lista:', SIZE)

del LIST[2]
print(LIST)

LIST[2] = 'tres'
print(LIST)

# Concatenar dos listas

LIST += ['ocho', 9, True, False]
print(LIST)

# añadir elemento a una lista

LIST.append('elemento nuevo')
print(LIST)

LIST.remove(False)
print(LIST)

LIST.reverse()
print(LIST)

LIST.reverse()
LIST.insert(3, 'cuatro')
print(LIST)

