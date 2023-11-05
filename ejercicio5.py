#idem , pero agregando la frase al comienzo del archivo 
# original (de nuevo , sin hacer una copia del archivo 
# )
def agregarFraseAlComienzo(archivoQueLeere : str , frase : str)->None:
    archivo = open(archivoQueLeere,"r")
    lista = archivo.readlines()
    lista.insert(0,frase+"\n")
    archivo.close 
    archivo = open(archivoQueLeere,"w")
    for linea in lista :
        archivo.write(linea)

agregarFraseAlComienzo("textoPrueba.txt" , "NALDOOOO")