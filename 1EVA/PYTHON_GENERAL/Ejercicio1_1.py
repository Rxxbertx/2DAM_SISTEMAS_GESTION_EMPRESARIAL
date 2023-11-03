
def sumaNum(num:int):
    suma = 0
    
    for i in range(num+1) :
        if i%2==0:
            suma+=i
    return suma


def sumaNumRecursiva(num:int):
    if num == 0:
         return 0
    elif num % 2 == 0:
         return num + sumaNumRecursiva(num - 1)
    else:
        return sumaNumRecursiva(num - 1)

print(sumaNumRecursiva(7))

   
print(sumaNum(8))
   