import yaml
from yaml.loader import SafeLoader


def read_yaml(path: str) -> dict:
    """permite leer un archivo yaml y devolver el contenido como dict

    :param path: ruta archivo
    :type path: str
    :return: rdiccionario con los datos YAML, de lo contrario devuelve Ninguno
    :rtype: dict
    """
    content: dict = None
    try:
        with open(path) as file:
            content = yaml.load(file, Loader=SafeLoader)
    except Exception:
        content = None
    return content
