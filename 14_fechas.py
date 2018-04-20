"""
trabajar con fechas en python
"""

import time

seconds = time.time()
print('número de ticks desde las 12:00 del 1 de Enero de 1970:', seconds)

# hora local

local_time = time.localtime(seconds)
print(local_time)
print(type(local_time))

# hora local formateada

asctime = time.asctime(local_time)
print(asctime)

# hora con formato personalizado

date_format ='%d-%b-%Y a las %H: %M: %S'
date_formated = time.strftime(date_format, time.gmtime(seconds)) #strf= string format time
print(date_formated)