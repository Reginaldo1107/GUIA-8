# Dado un archivo de texto implementar una funcion que 
# escribe un archivo nuevo llamdo reverso.txt que tiene las 
# mismas lineas que el original , pero en orden inverso 
#ejemplo : si el archivo es 

# Esta es la primera linea
#Y esta es la segunda linea

#########
#debe generar 
#########

#Y esta es la segunda linea
#Esta es la primera linea 

def reverso (archivoLectura : str) -> None:
    archivoLeer = open(archivoLectura,"r")
    archivoEscritura = open("reverso.txt","w")
    
    listaDeLineas = archivoLeer.readlines()
    listaReverso = []
    for linea in listaDeLineas :
        listaReverso.insert(0,linea)

    for linea in listaReverso :
        archivoEscritura.write(linea) 
    
    archivoLeer.close()
    archivoEscritura.close()
    
reverso("textoPrueba.txt")    