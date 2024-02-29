import argparse
import os

def verificar_existencia_archivo(archivo):
    # verificar si el archivo existe
    if not os.path.exists(archivo):
        raise argparse.ArgumentTypeError(f"El archivo {archivo} no existe.")
    return archivo

def main():
    # crear un objeto ArgumentParser
    parser = argparse.ArgumentParser(description='script de ejemplo con argparse')

    # agregar un argumento --archivo
    parser.add_argument('--archivo', type=verificar_existencia_archivo, required=True,
                        help='Ruta al archivo a procesar')

    # analizar los argumentos de la línea de comandos
    args = parser.parse_args()

    # imprimir la ruta del archivo proporcionada
    print(f'ruta del archivo proporcionada: {args.archivo}')

if __name__ == '__main__':
    main()