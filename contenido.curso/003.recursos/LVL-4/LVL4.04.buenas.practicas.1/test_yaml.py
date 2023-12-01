import json
from typing import Any, Dict
from snipcode.yaml.uso_yaml import leer_yaml

print("\n -- simple --\n")
contenido: Dict[str, Any] = leer_yaml("config/simple.yaml")
print(json.dumps(contenido, indent=4))

print("\n -- mensajes --\n")
contenido: Dict[str, Any] = leer_yaml("config/mensajes.yaml")
print(json.dumps(contenido, indent=4))

print(f"mensaje en ingles de error: ----> {contenido['en']['error']}")