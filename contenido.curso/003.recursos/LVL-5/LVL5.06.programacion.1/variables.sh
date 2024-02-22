# asignado variable al resultado
# regla de oro: rutas en absoluto, igual que los archivos
RUTA_ACTUAL=$(pwd)
hola="XYZ"
echo $hola
FECHA_LOG=$(date +"%d%m%Y")
RUTA_LOG="$RUTA_ACTUAL/transacciciones_$FECHA_LOG.log"

# nota: en el .sh puede ejecutar comandos del OS, eje cp, mkdir, etc
echo "la ruta actual es: $RUTA_ACTUAL" > $RUTA_LOG
echo "ruta log: $RUTA_LOG"  >> $RUTA_LOG

# texto
texto="texto"

# numero
declare -i edad
edad=12



# listas 

# valores inicializados
lista_1=(1 2 3 4 5)

# definir lista vacia  <! lista por indice
declare -a lista_2

# los indices no genera problema su no existen
lista_2[3]=1

echo "valor variable texto    : $texto"
echo "valor variable numero 1 : $edad"
echo "valor variable numero 2 : ${edad}"
# si una lista se imprime directamente, siempre mostrara el primer
# valor unicamente, los demas se omiten.
echo "valor variable lista 1  : $lista_1"
echo "valor variable lista 2  : $lista_2"

# truco, normalmente cuando vean ${} hace referencia a dos cosas
# 1. que esta llamando o se esta asegurando que esta llamando la variable
# con el nombre exacto, ejemplo ${NOMBRE_VARIABLE} un toque mas de seguridad
# 2. las llaves activan la opción de metodos a la variable
# metodos de las listas

echo "001. imprimiendo por index     : ${lista_1[2]}"
# devuelve una lista
echo "002. imprimiendo en lista #1   : ${lista_1[@]}"
echo "002. imprimiendo en lista #2   : ${lista_2[@]}"
# el * imprime en texto
echo "003. imprimiendo en lista #1   : ${lista_1[*]}"
echo "003. imprimiendo en lista #2   : ${lista_2[*]}"

# el ! imrimir los indices de la lista
echo "004. imprimiendo indices #1    : ${!lista_1[@]}"
echo "004. imprimiendo en lista #2   : ${!lista_2[*]}"

# el # cantidad de elementos en la lista
echo "005. imprimiendo indices  #1   : ${#lista_1[@]}"
echo "005. imprimiendo en lista #2   : ${#lista_2[*]}"

# el slices
echo "006. haciendo slices     #1    : ${lista_1[@]:1:3}"



# arrays asociativos tienen llave y valor (es como un diccionario en python)

declare -A bootcamp
bootcamp[curso]="linux elemental"
bootcamp[osp]="ubuntu"

echo ""
echo "listas asociativas"
echo ""
echo "001. imprimiendo valor por llave     : ${bootcamp[curso]}"
# devuelve una lista
echo "002. devuelve elementos en una lista   : ${bootcamp[@]}"

# el * imprime en texto
echo "003. imprimiendo en lista aninada #1   : ${bootcamp[*]}"


# el ! imrimir los indices de la lista
echo "004. imprimiendo las llaves #1    : ${!bootcamp[@]}"


# el # cantidad de elementos en la lista
echo "005. imprimiendo cantidad  #1   : ${#bootcamp[@]}"
