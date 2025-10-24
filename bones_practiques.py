#!/usr/bin/env python
'''Divisió Entera. Fa la divisió de dos nombres enters
Programació - 1r Batxillerat - Curs 2023-24
El programa demana que introdueixis un dividend enter i un divisor enter.
A continuació, calcula el quocient i el residu de la divisió.
Després mostra per pantalla la divisió que ha intoduit l'usuari, el quocient
i el residu'''

__author__ = "Gabriel Casademunt Alexanderson"
__email__ = "GCasademunt@instituticaria.cat"
__date__ = "22/10/2025"

dividend = int(input("Dividend:"))
divisor = int(input("Divisor:"))
quocient = dividend // divisor
residu = dividend % divisor

print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")
