import os
from pathlib import Path
from xml.dom.minidom import Document 

#Se obtiene el ruta en la que se trabaja
directorio_actual = Path.cwd()
ruta_actual = Path(directorio_actual)

def listar_documentos():
    for documento in ruta_actual.iterdir():
    
        if documento.is_file() and  documento.suffix == '.txt':
            print(documento.name)

def leer_documentos():
    nombre = input('¿Qué archivo quiere leer?: ')
    ruta_documento = directorio_actual / nombre

    with open(ruta_documento) as documento:
        archivo = documento.read()
        print(archivo)

def eliminar_documento():
    nombre = input('¿Qué archivo quiere eliminar?: ')
    ruta_documento = directorio_actual / nombre
    os.remove(ruta_documento)

print ('¿Qué desea hacer?')
print ('1) Listar documentos')
print ('2) Leer documento')
print ('3) Eliminar documento') 
print ('4) Terminar consulta') 

eleccion = int(input('Ingrese el número de la opción:'))

while eleccion:
    if eleccion == 1:
        listar_documentos()
    elif eleccion == 2:
        leer_documentos()
    elif eleccion == 3:
        eliminar_documento()
    elif eleccion == 4:
        print ('Fin de la consulta')
        break
    eleccion = int(input('Ingrese el número de la opción:'))