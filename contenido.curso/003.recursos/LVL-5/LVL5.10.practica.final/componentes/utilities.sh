#!/bin/bash

function obtener_parametros(){
    echo "nombre='Live Linux Demo'"
    echo "fecha='$(date +'%d/%m/%Y %H:%M:%S')'"
    echo "app=$0"
}

function ayuda(){
    echo ""
    echo "parametros invalidos"
    echo "optiones permitidas: "
    echo ""
    echo "$0 [instalar|-i|rollback|-r]"
    echo "por favor revisar parametros"

}