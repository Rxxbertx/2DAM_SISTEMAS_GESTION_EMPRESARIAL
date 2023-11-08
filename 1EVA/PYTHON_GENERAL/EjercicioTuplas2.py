
"""
Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

"""

precios:int = [50, 75, 46, 22, 80, 65, 8]

def preciosMayorMenor(precios:[int]):
    
    print(sorted(precios)[0])
    print(sorted(precios)[-1])
    
preciosMayorMenor(precios)

