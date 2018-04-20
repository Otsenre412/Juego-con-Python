"""
Ejemplos para trabajar con diccionarios
"""

ALUMNO = {
    'nombre': 'Ernesto',
    'edad': 25,
    'clase': 'python'
}

print(ALUMNO)
print(ALUMNO['nombre'])
print(ALUMNO['edad'])
print(ALUMNO['clase'])

ALUMNO['edad'] = 20
print(ALUMNO)

ALUMNO['sexo'] = ' masculino'
print(ALUMNO)

del ALUMNO['sexo']
print(ALUMNO)

ALUMNO.clear()
print(ALUMNO)


