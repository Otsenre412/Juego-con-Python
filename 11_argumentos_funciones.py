"""
diferentes maneras de usar argumentos
"""

# argumentos posicionales

def hi(name):
    print('hola', name)

# hi() esto falla porque name es obligatorio

# valores por defecto

def f(n= 'uno'):
    print(n)

f()
f(2)

def f2(one, two, three=3):
    print('one:', one, 'two:', two, 'three:', three)

f2('pepe', 'lola', 45)

# usr argumentos como keyword

f2(
    three= 'Carmen',
    one= 'Pedro',
    two= 'Sara'
)

def f3(name, *args):
    print('hola', name)
    print(args)

f3('Pedro', 20, 30, 40, True, False, 'Hola')

t = ('Pedro', 20, 30, 40, True, False, 'Hola')
f3('Ernesto', t)

def f4(*args):
    print(args)

f4('uno')
f4('uno', 2, 3, 4)
f4(True, False)

def f5(**kwars):
    print(kwars)

f5(nombre= 'Ernesto', edad= 25, clase= 'python')

O = {'nombre': 'Ernesto', 'edad': 25, 'clase': 'python'}

f5(**O)