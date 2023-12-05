import win32api

#Cambiar el horario.
win32api.SetSystemTime(2020, 12, 5, 24, 18, 30, 5, 1)

#Los parámetros van en orden y solo deben ser numeros enteros.
"""
Año: int,
Mes: int,
Día de la semana: int,
Día de calendario: int,
hora: int,
minuto: int,
segundo: int,
milisegundo: int
"""

print("¡El horario fue cambiado con éxito!")