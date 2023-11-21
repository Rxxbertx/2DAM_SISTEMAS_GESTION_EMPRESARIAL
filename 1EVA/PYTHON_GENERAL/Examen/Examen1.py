

"""Escribe un programa llamado operaciones que, dados dos números, 
realice las operaciones de suma, resta, multiplicación y división, 
e imprima los resultados  de una de las dos maneras que te muestro a continuación:"""

##ejercicio1

def operaciones(num1,num2):

    print (f"Suma: {num1+num2}")
    print (f"Resta: {num1-num2}")
    print (f"Multiplicacion: {num1*num2}")
    if num2==0:
        print("No se puede dividir entre 0")
    else:
        print (f"Division: {num1/num2}")

operaciones(5,2)

##ejercicio2

"""
Escribe un programa llamado es_primo() que determine si es primo o no, 
devolviendo verdadero si lo es y falso si no
"""

def esPrimo(num):
    
    for i in range(1,num+1):
        if num%i==0 and num is not i and i is not 1:
            return False
    
    return True

print(esPrimo(121))

"""
Implementa una función llamada utilidades_listas() que tome una lista de números y realice las siguientes operaciones:

    Muestra la lista original.
    Calcula la suma de los elementos.
    Encuentra el valor máximo y mínimo.
    Imprime la lista ordenada de menor a mayor.

"""


##ejercicio3



def utilidades_listas(lista:list):

    print(f"Lista original: {lista}")
    print("Suma de sus elementos:",sum(lista))
    print("Valor máximo:",max(lista))
    print("Valor minimo:",min(lista))
    print("Lista ordenada: ",sorted(lista))

utilidades_listas([5,3,1,2])


"""
Desarrolla un programa que simule una agenda de contactos. 
Utiliza un diccionario donde las 
claves son los nombres y los valores son sus números de teléfono. 
Permite al usuario agregar nuevos contactos, 
buscar un número de teléfono por nombre y eliminar contactos.

Apóyate en este código para que te sea más sencillo:

"""
##ejercicio4


agenda = {}

agenda["roberto"]=12345678

def agregarContacto():
    
    while(True):

        clave:str=str(input("Dime el nombre del contacto que deseas agregar: (para salir escriba X)"))
            
        if clave == "X" or clave == "x":
            return
        
        if not clave:
            print("Error, debes ingresar un nombre valido")
            continue
        
        valor:str=str(input(f"Ingresa el telefono para el contacto: {clave}: "))

        if not valor.isnumeric() or len(valor)<9:
            print("Error, debes ingresar un telefono valido")
            continue
        
        agenda[clave]=valor

        print("CONTACTO AGREGADO CORRECTAMENTE")

def buscarContacto():

    while(True):

        clave:str=str(input("Dime el nombre del contacto que deseas buscar: (para salir escriba X)"))
            
        if clave == "X" or clave == "x":
            return
        
        if not clave:
            print("Error, debes ingresar algo")
            continue

        if not agenda.get(clave):
            print(f"{clave} no existe")
            continue
        
        print(f"Contacto: {clave} Telefono: {agenda[clave]}")

def eliminarContacto():


    while(True):

        clave:str=str(input("Dime el nombre del contacto que deseas eliminar: (para salir escriba X)"))
        
        if clave == "X" or clave == "x":
            return
        

        if not clave:
            print("Error, debes ingresar algo")
            continue
            
        if not agenda.get(clave):
            print(f"{clave} no existe")
            continue

        del agenda[clave]
        print(f"CONTACTO {clave} ELIMINADO CORRECTAMENTE")

def mostrarContactos():

    print("CONTACTOS EN LA AGENDA")

    if not agenda.items():
        print("NO TIENES NIGUN CONTACTO CREADO")
        return

    for clave,valor in agenda.items():
        print(f"Nombre: {clave}, Telefono: {valor}")


while True:
    print("\n*** Menú de Agenda ***")
    print("1. Agregar contacto")
    print("2. Buscar contacto por nombre")
    print("3. Eliminar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        agregarContacto()
    elif opcion == "2":
        buscarContacto()
    elif opcion == "3":
        eliminarContacto()
    elif opcion == "4":
        mostrarContactos()
    elif opcion == "5":
        SystemExit
    else:
        print("Opción no válida, seleccione del 1 al 5")






