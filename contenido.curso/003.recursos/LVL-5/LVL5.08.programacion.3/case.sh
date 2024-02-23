
#!/bin/bash
# vamos a simular que vamos a realizar una accion, a partir de un parametro
# proceso para mover info o mantenimiento del os

OPCION=$1
echo "valor de entrada: $OPCION"
case $OPCION in
    "mover")
        echo "entro a la opción mover"
    ;;

    "copiar")
        echo "entro a la opción copiar"
    ;;

    "renombrar")
        echo "entro a la opción renombrar"
    ;;

    *) 
    # asociarlo con el else
    echo "opcion: ** $OPCION -- desconocido"
    ;;
esac