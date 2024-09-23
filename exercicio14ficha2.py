# ler valores

a = int(input("insira a:  "))
b = int(input("insira b:  "))
c = int(input("insira c:  "))

# apresentar os valores por ordem crescente

if (a < b and a < c): 
    if (b < c): 
        print(a, b, c)
    else:   
        print(a, c, b)
        

if (b < a and b < c): 
    if (a < c): 
        print(b, a, c)
    else: 
        print( b, c, a)
        
if (c < a and c < b): 
    if (a < b):
        print (c, a, b)
        else 
        print (c, b, a)
        