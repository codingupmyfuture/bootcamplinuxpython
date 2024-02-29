
function mensaje_ayuda(){
    echo ""
    echo "comando invalido, por favor ejecutar:"
    echo ""
    echo "$0 [-h|help|--help]"
}

if [[ -z "$1" ]]; then
    echo "[FAIL] no envio un parametro"
    mensaje_ayuda
    exit 1
else
    case $1 in 
        -h|help|--help)
        echo "ejecutando ayuda"
        echo ""
        echo "I'm not a pray man, but if you are up there, save me superman!!"
        ;;
        *)
        mensaje_ayuda
        ;;
    esac
fi

# -h | help | --help