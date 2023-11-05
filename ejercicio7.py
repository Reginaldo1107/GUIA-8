#Implementar una funcion que lea un archivo de texto separado por comas , (comma-separated values , o .csv) que contiene las notas de toda la carrera de un grupo de alumnos y calcule el promedio final de un alumno dado , la funcion 
def promedioTotal(alumno :str) -> int :
    archivoCSV = open("textoDePruebasCSV.csv")
    sumaTotal :int = 0 
    cantidadDeMaterias :int = 0 
    texto :list = archivoCSV.readlines() #todos los csv
    listaDeNumeros :list = []
    
    for lineaString in texto :
        lineaLista :list = lineaString.split(",")
        
        if(lineaLista[0] == alumno):
            cantidadDeMaterias +=1
            sumaTotal+=int (lineaLista[3])
            
            
    
    return sumaTotal/cantidadDeMaterias    
        

print(promedioTotal("Reginaldo"))