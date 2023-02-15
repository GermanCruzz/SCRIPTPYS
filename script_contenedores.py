import sys
#SCRIPT PARA GESTIONAR CONTENEDORES

#MAXIMO 5 CONTENEDORES:
    #SI TENGO MÁS DE 5 CONTENEDORES. QUE ELIMINE LOS + ANTIGUOS
    #EXCEPTO CONTENEDORES QUE CONTENGAN LA PALABRA DB

#LOS CONTENEDORES SE IRÁN AÑADIENDO COMO ARGUMENTOS AL FICH CONTENEDORES.TXT

#CONTENEDORES.TXT
#./script_contenedores.py ID_CONTENEDOR NOMBRE_CONTENEDOR, DESCRIPCION_CONTENEDOR

#PASO1. Recibir los 3 argumentos + nombre.py

#arg 1 -> ID
#arg 2 -> nombre
#arg 3 -> descripcion

#PASO 2. Comprobar numero de contenedores guardados en el fichero
#Buscamos una funcion que cuente el número de lineas.

#PASO 3. Si hay <5 -> Abrir fichero en modo a y Escribe el contenedor directamente
        #Si hay 5 o mñas borro el contenedor más antiguo  -> Solo si el cotenedor no contiene db. Si no 
        #lo tiene paso al siguiente.
        # y escribir el contenedor nuevo.

        
if len(sys.argv) < 4:
    print ("El programa necesita 4 argumentos.")
    exit(1)

ID_contenedor=sys.argv[1]
nombre_contenedor=sys.argv[2]
descripcion_contenedor=sys.argv[3]

fichero=open('contenedores.txt','r')
lineas=len(fichero.readlines())
print (lineas)
fichero.close

if (len(lineas)<5):
    fichero=open('contenedores.txt','a')
    fichero.write(ID_contenedor + ";" +  nombre_contenedor + ";"  + descripcion_contenedor + "\n")
    fichero.close
else :
    
    i=0
    for line in lineas:
        linea=line.split(";")
    nombre=linea[1]

    if not "db" in nombre:
        lineas.pop(i)
        lineas.append(ID_contenedor + ";" +  nombre_contenedor + ";"  + descripcion_contenedor + "\n")

        with open("contenedores-txt","w") as writefile:
            writefile.writelines(lineas)
            writefile.write("\n" + ID_contenedor + ";" +  nombre_contenedor + ";"  + descripcion_contenedor + "\n")

            exit(0)

            



