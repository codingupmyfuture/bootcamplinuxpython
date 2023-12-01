import argparse
parser = argparse.ArgumentParser(
                    prog='BootcampDemo',
                    description='validador de argumentos',
                    epilog='todos los derechos reservados.')

parser.add_argument('posicional', type=str, help='se envia posicionalmente')
parser.add_argument('-o', '--nombre_opcion',type=int, help='opción que toma un valor')

args = parser.parse_args()
print(args)