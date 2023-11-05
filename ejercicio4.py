# ejercicio 4 
#Dado un archivo de texto y una frase , implementar una funcion que la agregue al final del archivo original (sin hacer una copia)
def agregarFrase (archivoLectura : str , frase :str )->None:
    archivoparaLeer = open(archivoLectura,"r")
    listaMasElAgregado :list = []
    for linea in archivoparaLeer.readlines() :
         listaMasElAgregado.append(linea)
    
    listaMasElAgregado.append(frase)
    archivoparaLeer.close()
    
    archivoparaLeer = open(archivoLectura,"w")
    
    for linea in listaMasElAgregado:
        archivoparaLeer.write(linea)
        
agregarFrase("textoPrueba.txt","\nBALDERA")
         
        