#!/bin/bash

# simple
elementos=(1 2 3 4 5 6 7 8 9 10)
echo "cantidad de elementos: ${#elementos[@]}"

# iterando lista
for numero in ${elementos[@]}; do 
    echo "el numero es $numero"
    echo "---------------------"
done

# textos no se segmentan por cada caracter (como python)
NOMBRE="abcd"
for valor in $NOMBRE; do 
    echo $valor
done


# iterar con el sistema operativo absoluto
for archivo in $(ls /tmp/); do 
    echo "archivo : $archivo"
    echo "peso    :  $(du -h /tmp/$archivo)"
done

echo ""
echo "relativo"
echo ""
echo "ruta: $(pwd)"
echo ""
# iterar con el sistema operativo absoluto

for archivo in $(ls); do 
    echo "archivo : $archivo"
    echo "peso    :  $(du -h $archivo)"
done


# leyendo archivos
RUTA_ARCHIVO="$(pwd)/log.txt"
echo "DESC" > $RUTA_ARCHIVO
echo "creando un log" >> $RUTA_ARCHIVO
echo "linea xyz" >> $RUTA_ARCHIVO
echo "linea abc" >> $RUTA_ARCHIVO

for linea in $(cat $RUTA_ARCHIVO | head -n2); do 
    echo "contenido --->>> $linea"
done
