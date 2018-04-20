
from colorama import init, Fore, Back, Style

init()

print('hola')
print(Fore.BLUE + 'esto es azulito')           # cambiar el color de las letras
print(Fore.CYAN + 'mas cosas en colorimes')
print(Fore.RED + 'y esto es rojo')

print(Back.GREEN + 'fondo verde')              # cambiar el fondo de la frase anterior

print(Style.RESET_ALL)
print('hola')