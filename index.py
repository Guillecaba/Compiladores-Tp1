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
        resultado= x + y
    else:
        print('ola')
        #return resultado
     
    return resultado
   
    
      

def c():
    global preanalisis
    if (ord(preanalisis) >= 97 and ord(preanalisis) <= 122):
        x=preanalisis
        preanalisis=coincidir(x)
        return ord(x)
    else:
        return


def coincidir(t):
    global preanalisis
    global index
    if preanalisis != 'A':
        print('Preanalisis '+preanalisis)
        print('Coincidir ' +t)
    
    if(preanalisis == t):
        print(index)
        index+=1
        if(index <= len(cadena)-1):
            
            return cadena[index]
            
        else:
            return 'A'
      





print(preanalisis)
resultado= r()
print(resultado)
    

