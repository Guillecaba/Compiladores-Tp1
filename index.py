index=0
cadena='abc'
print(len(cadena))
preanalisis= cadena[0]

def r():
    global preanalisis
    resultado= 0
    if (ord(preanalisis) >= 97 and ord(preanalisis) <= 122):
        x= c()
        y= r()
        return x + y
    else:
        return 0;
   
def c():
    global preanalisis
    x=preanalisis
    preanalisis= coincidir(x)
    return ord(x)

def coincidir(t):
    global preanalisis
    global index
   
    print('Preanalisis '+preanalisis)
    print('Coincidir ' +t)
    
    if(preanalisis == t):
        print(index)
        index+=1
        if(index <= len(cadena)-1):
            return cadena[index]
        else: 
            return ' '
         
      





print(preanalisis)
resultado= r()
print(resultado)
    

