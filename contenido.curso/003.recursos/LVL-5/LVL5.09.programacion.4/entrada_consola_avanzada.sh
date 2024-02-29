#!/bin/bash

read -p "ingrese edad      : " valor
read -p "ingrese su nombre : " texto




# cuando usted ingresa algo por consola, usted lo validar

# validar si el dato es numerico
if [[ "$valor" =~ ^[0-9]+$ ]]; then
    echo "[OK] variable valor valida, valor : $valor"
else
    echo "[FAIL] variable valor invalida, valor : $valor"
fi

# validar si el texto esta vacio
if [[ -z "$texto" ]]; then
    echo "[FAIL] variable texto invalida, valor : $texto"
else
    echo "[OK] variable texto valida, valor : $texto"
fi

# input: fecha,
# validacion: validar que el texto ingresado tenga un formato x de fechas
# EJE: 27/02/2024, %d/%m/%A

