#1,1
#Una funcion llamada contarLineas (in nombreArchivo :str ) -> int que cuenta y devuelva la cantidad de lineas de texto del archivo dado 
def contarLineas(archivoLectura :str) -> int :
    archivoLectura = open(archivoLectura,"r",encoding="utf8")
    contador:int = 0
    for linea in archivoLectura.readlines() :
        contador+=1
    archivoLectura.close()
    return contador    
#print(contarLineas("textoPrueba.txt") )

#1,2
#Una funcion existePalabra (in palabra : str , in nombreArchivo : str) ->bool , que dice si una palabra existe en un archivo de texto o no ?
def existePalabra(palabra : str , nombreArchivo : str) ->bool :
    archivoLectura = open (nombreArchivo,"r",encoding="utf8")
    listaDeFilas :list = []
    laPalabraEsta :bool = False
    
    for linea in archivoLectura.readlines():
        listaDeFilas.insert(0,linea)
    
    
    for i in range (len(listaDeFilas)):
        if(palabra in listaDeFilas[i]  ):
            laPalabraEsta = True
    return laPalabraEsta    

def existePalabra2_0(palabra : str , nombreArchivo : str) ->bool :
     
    archivo = open(nombreArchivo,"r")
    estaEnElArchivo :bool = False 
    for linea in archivo.readlines():
        if palabra in linea :
            estaEnElArchivo = True
            
    return estaEnElArchivo        
print(existePalabra2_0("naldo","textoPrueba.txt"))


#1.3 Una funcion cantidadAparaciones (in nombreArchivos : str , in palabra :str) -> int que devuelve la cantidad de apariciones de una palabra en un archivo de texto 

def cantidadAparaciones (nombreArchivos : str , palabra :str ) -> int :
    archivoLectura = open(nombreArchivos,"r",encoding="utf8")
    #listaDeFilas :list = []
    conteoTotal :int = 0
    for linea in archivoLectura.readlines():
        conteoTotal+= linea.count(palabra)
          
    return conteoTotal    

#print(cantidadAparaciones("textoPrueba.txt","naldo"))









