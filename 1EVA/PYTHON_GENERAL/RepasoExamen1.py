

##ejercicio 4
"""
def sacarLista(lista) -> str:
    if not lista:
        return ""
    else:
        return str(lista[0]) + sacarLista(lista[1:])

numeroGanador = input("Introduce numero ganador: ")
lista = [int(x) for x in numeroGanador]
lista.sort()
numeroGanador = sacarLista(lista)

print(numeroGanador)
"""

##ejercicio5



def sacarNumeroConComa(numeros, indice):
    if indice == len(numeros) - 1:
        return str(numeros[indice])
    else:
        return str(numeros[indice]) + "," + sacarNumeroConComa(numeros, indice + 1)

numeros = [x for x in range(1, 11)]
numeros.reverse()
print(sacarNumeroConComa(numeros, 0))

##ejercicio6

asignaturas:list=["Matematicas","Fisica","Quimica","Historia","Lengua"];
def preguntarUser():
    print("NOTAS DE ASIGNATURAS")
    for i in asignaturas:
        nota=(int(input("NOTA DE "+i+": ")))
        if (nota>4):
            asignaturas.remove(i)
    print ("ASINGNATURAS PENDIENTES")
    for i in asignaturas:
        print("-----"+i)

##preguntarUser();

##ejercicio7

abecedario = [chr(letra) for letra in range(ord('a'), ord('z') + 1)]

# Eliminar letras cuyas posiciones son múltiplos de 3
abecedario_filtrado = [letra for i, letra in enumerate(abecedario, start=1) if i % 3 != 0]

# Mostrar la lista resultante
print(abecedario_filtrado)

##DICCIONARIOS
##ejercicio 5

diccionario:dict={'Matemáticas': 6, 'Física': 4, 'Química': 5}

for key,valor in diccionario.items():
    print (f"{key} tiene {valor} créditos")

print(f"numero total de creditos: {sum(diccionario.values())}")

##ejercicio 6


personas:dict={}
print(len(personas))

def añadirPersona():
    
    personas[str("persona"+str(len(personas)))]={}




def modificarPersona():
     

    salir = False
    
    while(not salir):
        print ("SELECCIONA A QUE PERSONA QUIERES MODIFICAR")
        
        for i in personas:
            print (i)
        
        
        
        
        numero = input("----NUMERO: ")
        if personas[numero] is None:
            print("ERROR ESA PERSONA NO EXISTE")
        else:
            return
                    








salir=False

while(not salir):
    print("QUE DESEAS HACER? (AÑADIR PERSONA NUEVA(1),AÑADIR DATOS A UNA YA CREADA(2))")
    opcion:int = int(input())
    if opcion == 1:
        añadirPersona()
    elif opcion==2:
        modificarPersona()
    else:
        salir=True
        
    














