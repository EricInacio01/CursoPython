# Condicionais em Python
"""
==== [ OPERADORES LÓGICOS ] ====
- Igual: ==
- Maior 

"""

N = int(input("Informe quantos minutos restam para acabar o expediente"))
A = int(input("Informe quantos minutos são necessários para fabricar o 1° presente"))
B = int(input("Informe quantos minutos são necessários para fabricar o 2° presente"))

if N >= (A + B):
    print("Farei hoje!")
else:
    print("Farei amanhã")

