
# codigo solo UNIX (mac & linux)

# tomo la ubicacion de site-packages
SPACKAGES=$(python -c "import site; print(site.getsitepackages()[0])")

# elimino si existe algo
rm -rf $SPACKAGES/bootcamp 2> /dev/null

# muestro la ruta de site-packages
echo $SPACKAGES

# creo el modulo
mkdir $SPACKAGES/bootcamp
touch $SPACKAGES/bootcamp/__init__.py
cp demo.py $SPACKAGES/bootcamp

# asigno permisos
chmod 777 -R $SPACKAGES/bootcamp

# muestro contenido
tree $SPACKAGES/bootcamp
echo ""
echo "[ejecutando ....]"
echo ""

# ejecuto el archivo python
python libreriapropia.py

echo ""
echo "[fin ....]"