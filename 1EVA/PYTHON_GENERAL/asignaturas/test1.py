#eje1


#eje2
var = "Hello World"
print(var)

#eje3
"""Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo 
    introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre
    que el usuario haya introducido.
"""

nombre = input("¿Cual es tu nombre? ")
print("¡ Hola, " + nombre + "!")


#eje4
"""
Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética
.
"""
operacion = (3+2)/(2*5)**2
print(operacion)

#eje5
"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
Después debe mostrar por pantalla la paga que le corresponde.
"""

horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce tus salari por hora:"))
print("Tu paga es de: " + str(horas*coste)) #str() convierte a string

#eje6
"""
Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla
la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada
de la siguiente forma:
"""

entero = float(input("numero entero"))
print(str(float(entero*(entero+1)/2)));



#eje7
"""
    
    Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
    calcule el índice de masa corporal y lo almacene en una variable, 
    y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> 
    es el índice de masa corporal calculado redondeado con dos decimales.
    
"""
    
    
peso = float(input("dame tu peso en kg pelon"))
estatura = float(input("dame tu estatura en metros pingas"))
imc = round(float(peso)/(float(estatura)**2),2)
print("TU IMC ESSSSSSSSSSSSSSSSSSSSSSSSS: "+str(imc))
    
    

"""
Ejercicio 10

Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

"""

num = int(input("dame un numero perro"));
def parImpar(num):
    
    if num % 2 == 0:
        return True
    else:
        return False

    
try:{
    print(f"tu numero {num} es {'PAR' if parImpar(num) else 'IMPAR'}")};
except ValueError:{
    print("error")}
    
    
