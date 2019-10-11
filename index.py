#Cadena de racteres formado por el alfabeto {a,b,c,..,z} y retorna el valor de la suma ASCII de los caracteres que la forman. Ejemplo abc 294

# Caracter de la cadena => R = Cx + Rx 
# Caracter vacio => Rx = 0
def r():
    global preanalisis
   
    if(preanalisis != None):
        x= c()
        y= r()
        return x + y
    else:
        return 0;

# C-> a | b | c |..|z
# Por ejemplo  Cx-> 97 
# Retorna en valor ASCII del caracter 
# Si el caracter no esta dentro del alfabeto lanza un mensaje de error de sintaxis 
def c():
    global preanalisis
    
    if (ord(preanalisis) >= 97 and ord(preanalisis) <= 122):
        x=preanalisis
        coincidir(preanalisis)  
        return ord(x)
    else:
         raise Exception('Error de sintaxis')


# Comprueba los terminales,  avanza al siguiente terminal de entrada  si hay una coincidencia con el simbolo de preanalisis
# en caso contrario retorna una excepcion        
def coincidir(t):
    global preanalisis
    global index
    
    if(preanalisis == t):
        if(index < len(cadena)-1):
            index+=1
            preanalisis=cadena[index]
        else: 
            preanalisis=None
    else:
        raise Exception('Error de Sintaxis')     




print("Traducción dirigida por la sintaxis,retorna el valor de la suma ASCII de los caracteres que forman una cadena de alfabeto de [a,b,...,z] ")
# Ingresar la cadena
# Cadenas vacias son un error de sintaxis
while(True):
    try:
        print('Ingresa la cadena: ')
        cadena=input()
        index=0
        print('La cadena ingresada fue: ',cadena)
        if(index <= len(cadena)-1 and len(cadena) > 0):
            preanalisis= cadena[index]   
        else:
            raise Exception ('Error de sintaxis')
        print("El resultado es ",r())
    except Exception as e:
        print(e)

    



    

