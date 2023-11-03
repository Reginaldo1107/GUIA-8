
# ejercicio 2   
##########################################################################################################
def es_comentario(texto:str) -> bool: 
    for letras in texto : 
        if letras != ' ' :
            if letras == '#': 
                return True
            return False   
    return False      

def clonarcomentarios(nombre_archivo:str) -> None:  
    archivo_imput = open(nombre_archivo,"r") 
    archivo_ouput = open ("prueba2.txt","w" ) 
    for texto in archivo_imput.readlines() : 
        if not es_comentario(texto) : 
            archivo_ouput.write(texto)

    archivo_imput.close()
    archivo_ouput.close()

#clonarcomentarios("textoPrueba.txt")
#############################


####################
#MI MODO , CON split()
####################
def clonar_sin_comentario(nombreArchibo : str )->None:
    archivoLeer = open(nombreArchibo, "r")
    archivoEscribir = open("naldoEscritura.txt","w")
    for linea in archivoLeer.readlines():
        reduccionLinea :str  = linea.lstrip()        
        if(reduccionLinea[0] != "#"):
            archivoEscribir.write(linea)
    
    archivoLeer.close()
    archivoEscribir.close()



clonar_sin_comentario("textoPrueba.txt")
##########################################################################################################
