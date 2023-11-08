import sys
import json

try:
    1/0
except Exception as ex:
    # santo grial, poco conocido  sys.exc_info()
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback_details = {
        'nombre_archivo' : exc_traceback.tb_frame.f_code.co_filename,
        'linea_nro'      : exc_traceback.tb_lineno,
        'modulo'         : exc_traceback.tb_frame.f_code.co_name,
        'tipo_error'     : exc_type.__name__,
        'excepcion'      :str(ex)
    }
    print(json.dumps(traceback_details, indent=4))
