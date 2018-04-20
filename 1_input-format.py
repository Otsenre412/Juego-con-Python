"""
Ejemplo para pedir input de usuario y formatear la respuesta
"""

PREGUNTA = '¿Cómo te llamas? '
RESPUESTA = input(PREGUNTA)

print('Hola', RESPUESTA, '¿Cómo estás?')

SALUDO = 'Welcome al curso de Python'
RESPUESTA_FORMATEADA = 'Hola {}, {}'.format(RESPUESTA, SALUDO)

print(RESPUESTA_FORMATEADA)