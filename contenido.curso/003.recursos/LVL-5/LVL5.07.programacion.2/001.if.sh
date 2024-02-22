#!/bin/bash

# validaciones de textos 
# condicional elemental
if [ "1" == "1" ]; then
    echo "[*****] entro a la condición"
fi

# condicional else
if [ "12" == "1" ]; then
    echo "[*****] entro a la condición"
else
    echo "[*****] val #2 no es igual"
fi

# condicional elif
if [ "12" == "1" ]; then
    echo "[*****] entro a la condición"
elif [ "2" == "1" ]; then
    echo "elif # 1"
elif [ "1" == "1" ]; then
    echo "entro a alguno de esos"
else
    echo "[*****] val #2 no es igual"
fi


# validaciones de numeros
edad=22
if [ $edad -eq 22 ]; then
    echo "la edad del profe es correcta!!"
fi


# validaciones de estados
# echo va ejecutar correctamente, yo validar el estado de esa ejecución
echo "validando estados en maquina"
if [ $? -eq 0 ]; then
    echo "programa ejecutado sin errores"
else
    echo "se detecto una ejecución erronea"
fi