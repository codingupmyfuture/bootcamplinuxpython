

VERSION_LARGA:str = f"1.0.0 generada el 23/11/2023"


@property
def version():
    return "1.0.0"


def saludar(nombre):
    return f"Hola, {nombre}!, enseñandote bobaditas!!"


def imprimir_logo():
    logo = """
                                                                                                             
  ____ ___  ____ ___ _   _  ____       _   _ ____       __  ____   __    _____ _   _ _____ _   _ ____  _____ 
 / ___/ _ \|  _ |_ _| \ | |/ ___|     | | | |  _ \     |  \/  \ \ / /   |  ___| | | |_   _| | | |  _ \| ____|
| |  | | | | | | | ||  \| | |  _ _____| | | | |_) _____| |\/| |\ V _____| |_  | | | | | | | | | | |_) |  _|  
| |__| |_| | |_| | || |\  | |_| |_____| |_| |  __|_____| |  | | | |_____|  _| | |_| | | | | |_| |  _ <| |___ 
 \____\___/|____|___|_| \_|\____|      \___/|_|        |_|  |_| |_|     |_|    \___/  |_|  \___/|_| \_|_____|
                                                                                                             
                                                                         

    """
    print(logo)