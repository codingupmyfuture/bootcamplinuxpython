#!/bin/bash

echo "nombre  ejecutable   : $0" # nombre del archivo
echo "primer  parametro    : $1" # parametro #1
echo "segundo parametro    : $2" # parametro #2
echo "imprimiendo todos v1 : $@" # todos los parametros(array)
echo "imprimiendo todos v1 : $*" # todos los parametros(string)
echo "contando parametros  : $#" # cantidad de parametros enviados

# 1. que se le envie un argumento a la shelll    [OK]
# 2. que ese argumento que es una archivo y exista
ARCHIVO=$1
if [ $# -eq 1 ]; then 
    echo "ok"
    if [ -e $1 ]; then
        du -h $1
    else
        echo "el archivo $1 no existe, valide por favor"
    fi

elif [ $# -gt 1 ]; then 
    echo "el programa $0 tiene mas parametros de los permitidos"
    exit 100
else
    echo "el programa $0 no tiene la cantidad de parametros que es 1"
    echo "nota: el archivo debe existir"
    echo ""
    echo "usage: $0 archivo.txt"
    exit 1
fi