
# código solo UNIX (Mac & Linux)

# tomo la ubicación de site-packages
SPACKAGES=$(python -c "import site; print(site.getsitepackages()[0])")

# elimino si existe algo
rm -rf $SPACKAGES/bootcamp 2> /dev/null

# muestro la ruta de site-packages
echo $SPACKAGES

# creo el módulo
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

# ejecuto el archivo Python
python libreriapropia.py

echo ""
echo "[fin ....]"