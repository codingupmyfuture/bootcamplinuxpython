
# constantes
CODIGO_OK=0
CODIGO_ERROR_FUNCION=-1
ROJO='\033[0;31m'
VERDE='\033[0;32m'
AMARILLO='\033[0;33m'
AZUL='\033[0;34m'
BLANCO='\033[0m'

# funciones utilitarias
function encabezado_bootcamp_1(){
    ASTERISCO="<<<****************************************************>>>"

    echo ""
    echo "$ASTERISCO"
    echo "    ___ _   _ __  __ ___ "
    echo "   / __| | | |  \/  | __|"
    echo "  | (__| |_| | |\/| | _| "
    echo "   \___|\___/|_|  |_|_|  "
    echo "  -------->"
    echo "           fecha : $(date +'%d/%m/%Y')"
    echo "           hora  : $(date +'%H:%M:%S')"
    echo "$ASTERISCO"
}

function encabezado_bootcamp_2(){
    ASTERISCO="<<<****************************************************>>>"

    echo ""
    imprimir_color $ROJO "$ASTERISCO"
    imprimir_color $AZUL "    ___ _   _ __  __ ___ "
    imprimir_color $VERDE "   / __| | | |  \/  | __|"
    imprimir_color $AMARILLO "  | (__| |_| | |\/| | _| "
    imprimir_color $BLANCO "   \___|\___/|_|  |_|_|  "
    imprimir_color $AZUL "  -------->"
    imprimir_color $VERDE "           fecha : $(date +'%d/%m/%Y')"
    imprimir_color $AMARILLO "           hora  : $(date +'%H:%M:%S')"
    imprimir_color $ROJO "$ASTERISCO"
}

function encabezado_bootcamp_3(){
ASTERISCO="<<<****************************************************>>>"
cat <<EOF
$ASTERISCO
     ___ _   _ __  __ ___ 
    / __| | | |  \/  | __|
   | (__| |_| | |\/| | _| 
    \___|\___/|_|  |_|_|  
    -------->
            fecha : $(date +'%d/%m/%Y')
            hora  : $(date +'%H:%M:%S')
$ASTERISCO
EOF
}


function probar_colores(){
    echo -e "${ROJO}Texto en rojo${BLANCO}"
    echo -e "${VERDE}texto en verde${BLANCO}"
    echo -e "${AMARILLO}texto en amarillo${BLANCO}"
    echo -e "${AZUL}texto en azul${BLANCO}"
}

function imprimir_color(){
    color=$1
    texto=$2
    echo -e "${color}${texto}${BLANCO}"
}