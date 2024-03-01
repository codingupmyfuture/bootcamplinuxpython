#!/usr/bin/env python3
import os
import sys
import argparse
import configparser


def verificar_existencia_archivo(archivo):
    # verificar si el archivo existe
    if not os.path.exists(archivo):
        raise argparse.ArgumentTypeError(f"El archivo {archivo} no existe.")
    return archivo

def obtejer_parametros() -> argparse:
    # crear un objeto ArgumentParser
    parser = argparse.ArgumentParser(description='app para obtener los parametros de un encabezado de .ini')

    # agregar un argumento --archivo
    parser.add_argument(
        '--archivo',
        type=verificar_existencia_archivo,
        required=True,
        help='ruta del archivo .ini a procesar'
    )
    
    parser.add_argument(
        '--encabezado',
        type=str,
        required=True,
        help='encabezado del archivo .ini'
    )
    return parser

def obtener_valores_encabezado(archivo: str, seccion: str) -> None:
    config = configparser.ConfigParser()
    # leer el archivo .ini
    config.read(archivo)
    parametros_seccion = config.items(seccion)
    print(f" INICIO [{seccion}]")
    for parametro in parametros_seccion:
        llave, valor = parametro
        print(f"\t{llave} = {valor}")
    else:
        print(f" FIN [{seccion}]")

if __name__ == '__main__':
    
    try:
        # 1. validamos parametros de entrada y que el archivo exista
        args = obtejer_parametros().parse_args()
        
        # 2. valiudar el archivo exista
        obtener_valores_encabezado(args.archivo, args.encabezado)
    except Exception as ex:
        print(ex)
        sys.exit(1)
