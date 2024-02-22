#!/bin/bash

numero=0

# while en linux
while [ $numero -le 10 ]; do 
    echo "[ITER] el numero es $numero"
    # sumar o contadores, utilizar el comando let
    let numero=$numero+1
done
