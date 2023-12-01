import argparse

# función definida por el usuario para validar si el valor es un número positivo
def es_numero_positivo(valor):
    try:
        numero = int(valor)
        if numero > 0:
            return numero
        else:
            raise argparse.ArgumentTypeError(f"{valor} no es un número positivo")
    except ValueError:
        raise argparse.ArgumentTypeError(f"{valor} no es un número")

# crear el objeto ArgumentParser
parser = argparse.ArgumentParser(description='Ejemplo de uso de argumentos con argparse')

# agregar argumentos
parser.add_argument('-f', '--file', help='Nombre del archivo', required=True)
parser.add_argument('-l', '--level', type=int, help='Nivel de detalle', default=1, choices=[1, 2, 3], dest='detalle')
parser.add_argument('-v', '--verbose', action='store_true', help='Modo verboso', dest='verboso')
parser.add_argument('-n', '--number', type=es_numero_positivo, help='Número positivo', dest='numero')

# analizar los argumentos
args = parser.parse_args()

# mostrar valores
print(f'archivo: {args.file}')
print(f'nivel de detalle: {args.detalle}')
print(f'modo verboso: {args.verboso}')
print(f'número positivo: {args.numero}')