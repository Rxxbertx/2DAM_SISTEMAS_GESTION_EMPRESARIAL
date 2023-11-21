

num = int(input("introduce numero"))

def triangulo(n:int):
    
    for i in range(1,n+1):
        temp:str="";
        
        for j in range(i,0,-1):
            temp+=str(j)+" "
            
        for e in range(n,i,-1):
            temp+=str(e)+" "
        print (temp)
        
triangulo(num)
            
            
    