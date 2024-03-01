
#!/bin/bash

# 0. variables
VARIABLES_TEST="$(pwd)/variables.txt"
ARCHIVO_TEST="$(pwd)/test.ini"
# 1. importar utilitarios
source ./componentes/utilities.sh
OPCION=$1

# 2. generar archivo de prueba y cargarlo
obtener_parametros > $VARIABLES_TEST
source $VARIABLES_TEST

# 3. generar archivo prueba
echo "[APP]" > $ARCHIVO_TEST
echo "nombre = $nombre" >> $ARCHIVO_TEST
echo "version = 1" >> $ARCHIVO_TEST
echo "" >> $ARCHIVO_TEST
echo "[RELEASE]" >> $ARCHIVO_TEST
echo "app = $app" >> $ARCHIVO_TEST
echo "fecha = $fecha" >> $ARCHIVO_TEST

# 4. instalar
cp -rf componentes/get_header.py /usr/local/bin/get_header
chmod +x /usr/local/bin/get_header

# pruebas

if [ $# -eq 1 ]; then

    case "$OPCION" in
        "instalar"|"-i")

        # sin parametros
        prueba_1=$(get_header)
        if [ $? -ne 0 ]; then
            echo "[ERROR 001] se presento errores por no enviar argumentos"
            echo ""
        fi

        ## arcivo no existe
        prueba_2=$(get_header --archivo a --header a)
        if [ $? -ne 0 ]; then
            echo "[ERROR 002] se presento errores por no enviar argumentos"
            echo ""
        fi


        ## arcivo existe, pero encabezado malo
        prueba_3=$(get_header --archivo $ARCHIVO_TEST --encabezado a)
        if [ $? -ne 0 ]; then
            echo "[ERROR 003] encabezado invalido, error: $prueba_3"
            echo ""
        fi

        ## todo ok
        prueba_4=$(get_header --archivo $ARCHIVO_TEST --encabezado APP)
        if [ $? -eq 0 ]; then
            echo "[OK 001] funcionando: $prueba_4"
            echo ""
        fi
        ;;
        "limpiar"|"--clear")
            rm -rf $VARIABLES_TEST 2> /dev/null
            rm -rf $ARCHIVO_TEST 2> /dev/null
            ;;
        "rollback"|"-r")
            rm -rf /usr/local/bin/get_header 2> /dev/null
            rm -rf $VARIABLES_TEST 2> /dev/null
            rm -rf $ARCHIVO_TEST 2> /dev/null
            
            echo "rollback realizado"
            echo "imprimiendo paquete instalado: "
            ls /usr/local/bin/ | grep get_
        ;;
        *)
            ayuda
        ;;

    esac

else
    ayuda
fi