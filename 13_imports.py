"""
ejemplos de como importar modulos y funciones python
"""

import utils # importar el metodo entero

utils.sumar(6, 8)
utils.restar(10, 4)

from utils import sumar #importar cosas o funciones concretas

sumar(5, 2)

from libs import bombing
bombing.where_are_the_bombs()

from libs.bombing import where_are_the_bombs, explosion #para llamar a varias funciones a la vez dentro de otro arcivo
where_are_the_bombs()
explosion()

from libs.bombing import *
explosion()