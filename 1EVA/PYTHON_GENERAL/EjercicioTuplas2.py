
def agregarContacto():
    
    nombre:str = str(input("NOMBRE DEL CONTACTO: "))
    
    if not nombre:
        print("nombre de contacto erroneo")
        return;
        
       
    try:
       telefono:int = int(input("Introduce numero de telefono"))
     
       contactos[nombre]=telefono
       
       print("contacto creado correctamente")
    
    except:
        print("numero incorrecto")
        return;
        
    


def buscarContacto():
    nombre:str = str(input("NOMBRE DEL CONTACTO A BUSCAR: "))
    
    if not nombre:
        print("nombre de contacto erroneo")
        return;
    
    try:
        tlfn=contactos.get(nombre)
        if not tlfn:
            print("ERROR NO EXISTE ESE CONTACTO") 
        else:
            print("NOMBRE: "+nombre+ "Telefono: "+contactos[nombre])
            
    except:
        print("ERROR NO EXISTE ESE CONTACTO")      
    
        







def salir():
    print("GRacias")
    exit()


contactos={};



while True:
    print("Menú:")
    print("1. Agregar un nuevo contacto")
    print("2. Buscar contacto por nombre")
    print("3. Salir del programa")

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
       
       agregarContacto();
         
    elif opcion == '2':
        
        buscarContacto();
        

    elif opcion == '3':
        
        salir();

    else:
        print("Opción no válida. Por favor, elige una opción del menú.")


    
