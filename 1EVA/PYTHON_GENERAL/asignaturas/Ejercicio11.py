
"""

Ejercicio 6

Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y 
los hombres con un nombre posterior a la N y el grupo B por el resto. 
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.


"""

error = True

while error:
    try:
        nombre = input("Por favor, ingresa tu nombre: ")
        sexo = input("Por favor, ingresa tu sexo (hombre/mujer): ")
        
        if nombre.isalpha() and sexo.isalpha():
            error = False
        else:
            error = True
    except ValueError: 
        print("Escribe de nuevo tu nombre y tu sexo de manera correcta")
        error = True


grupo = definir_grupo(nombre, sexo)
print("Perteneces al grupo " + grupo)

def definir_grupo(nombre, sexo):
    primer_letra = nombre[0].upper()
    if (sexo == 'mujer' and primer_letra < 'M') or (sexo == 'hombre' and primer_letra > 'N'):
        return 'A'
    else:
        return 'B'