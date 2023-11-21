##__repr__ si tiene esa fucnion lo imprime como tu le digas

##diferencia entre lista y tupla, t={1,2,3,4} una vez se crea la tupla no se modifica su tamaño
##diccionaria

pelis={"pesadillas":"Tim","Kill Bill":"Quentin tarantino","DJANGO":"Quentin tarantino","Reservoir Dogs":"Quentin tarantino","Fast & Furious":"Vin Diesel"}

for i in pelis.keys():
    if (pelis[i] == "Quentin tarantino"):
        print (f"\x1b[33m PELICULA: \033[0;m {i}, \033[35m DIRECTOR: \033[0;m {pelis[i]} ")
        
