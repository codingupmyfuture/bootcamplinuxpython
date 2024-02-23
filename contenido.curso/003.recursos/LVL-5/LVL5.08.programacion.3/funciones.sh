
# forma #1
saludo_1(){
    echo "hello my brave souls!! #1"
}

# forma #2
function saludo_2(){
    echo "hello my brave souls!! #2"
}

# entendiendo parametros de una funcion
function info(){
    echo "nombre de programa   --> $0" # retoma el nombre pero del programa
    echo "parametro de funcion --> $1"
    echo "parametro de funcion --> $3"
    echo "parametros           --> $@"
    echo "cantidad parametros  --> $#"
}

# antes de avanzar, se debe entender lo siguiente:
# 1. return en bash no devuelve valores, devuelven estados (hint: sensores)
# 2. para retornar valores se usa echo
# 3. todos los echos que se pongan dentro de la funcion hacen parte del valor que se retorna

function suma_elemental(){
    # creo variables con validacion
    declare -i numero_1
    declare -i numero_2

    # asigno argumentos enviados a la funcion
    numero_1=$1
    numero_2=$2

    # suma
    let suma=$numero_1+$numero_2

    # retorno valor
    echo $suma
    # echo "abcd" # tip #3
}


function suma_mejorada(){
    # creo variables con validacion
    declare -i numero_1
    declare -i numero_2
    declare -i estado
    declare -i suma

    if [ $# -eq 2 ]; then
        # asigno argumentos enviados a la funcion
        numero_1=$1
        numero_2=$2
        # suma
        let suma=$numero_1+$numero_2
    else
        suma=0
        estado=22
    fi

    echo $suma     # valor
    return $estado # estado
}


# saludo_1
# saludo_2
# info 1 2 3
#suma_elemental 1 3
#RESULTADO_SUMA=$(suma_elemental 4 6 4)
#echo "el resutaldo de la funcion es: $RESULTADO_SUMA"

#suma_mejorada 4 6
#echo $?

SUMA_MEJORADA=$(suma_mejorada 4 6 2)
echo "el estado de la ejecucion fue : $?"
echo "valor de la suma fue          : $SUMA_MEJORADA"