<img src="https://i.postimg.cc/cCjTSn8r/ss-cumf.png" alt="reporte" border="0"/>


# **MANEJO DE PROYECTOS CON GIT**

## **QUE ES UN REPOSITORIO?**
Un repositorio es un espacio centralizado donde se almacena, organiza, mantiene y difunde información digital, habitualmente archivos informáticos, que pueden contener trabajos científicos, conjuntos de datos o software.
<img src="https://centroderecursos.agesic.gub.uy/documents/portlet_file_entry/31472/Estructura+Repositorio+%281%29.png/8dc902c6-42f2-b9ce-bbea-83eb5e7bed5d?status=0&download=true
" alt="reporte" border="0"/>

## **QUE ES UN CONTROL DE VERSIONES?**

Un sistema de control de versiones (*o VCS, por sus siglas en inglés*), también conocido como sistema de control de revisiones o de fuentes, es una herramienta de software que monitoriza y gestiona cambios en un sistema de archivos.

<img src="https://miro.medium.com/v2/resize:fit:1400/0*qhbqSpJTrjqRNRSF.png
" alt="reporte" border="0"/>

## **QUE ES GIT**
Git es un sistema de control de versiones distribuido que te permite registrar los cambios que haces en tus archivos y volver a versiones anteriores si algo sale mal. Fue diseñado por `Linus Torvalds` para garantizar la eficiencia y confiabilidad del mantenimiento de versiones de aplicaciones que tienen un gran número de archivos de código fuente. **Principales repositorios** (*plataformas*) **online:**

<img src="https://hackmd.io/_uploads/BJSYgosBa.png" alt="reporte" border="0"/>

## **PARTES ELEMENTALES DE GIT**

* **rama(branch):** es una versión del código del proyecto sobre el que estás trabajando. Estas ramas ayudan a mantener el orden en el control de versiones y manipular el código de forma segura.

* **tronco(trunk):** es una práctica de gestión de control de versiones en la que los desarrolladores fusionan pequeñas actualizaciones de forma frecuente en un “tronco” o rama principal (main

* **feature branch**: la idea de esta practica es que el desarrollo de nuevas características de nuestro producto se va a realizar en ramas dedicadas para este propósito, en vez de realizarse directamente en la rama principal.

* **merge**: permite tomar las líneas independientes de desarrollo  e integrarlas en una sola rama.

* **pull request**: Es una funcionalidad de github (en gitlab llamada merge request y en bitbucket push request), en la que un colaborador pide que revisen sus cambios antes de hacer merge a una rama.

* **hotfix:** Es un parche o corrección de software que se utiliza para solucionar un problema específico dentro de un programa o sistema operativo.


## **FLUJO BÁSICO**
Entendamos como trabajan los equipos de una forma sencilla:

<img src="https://i.postimg.cc/3xtRvTWx/gitflow.png" alt="reporte" border="0"/>

si lo miramos técnicamente:

<img src="https://media.licdn.com/dms/image/C4D12AQE26eEIwEyuBw/article-cover_image-shrink_720_1280/0/1632978034642?e=2147483647&v=beta&t=x04TWwouE4hEBC0SJwedWMoW1sG9ONka4ReGzJz9CyA" alt="reporte" border="0"/>

## **USO Y COMANDOS BÁSICOS**

Al trabajar con GIT hay 3 formas que comúnmente se trabaja, para entender su usabilidad, mirémoslo en una clasificación con base a 5 estrellas:

* **Consola**: :star::star::star::star::star:
* **IDE (eje, VS Code)**: :star::star:
* **GitHub Desktop**:


### **CONSOLA**

1. menú de ayuda GIT
```bash
git -h
```

2. ver versión
```bash
git version
```

3. configurar git para sincronizar con el repo (***primera vez***)
```bash
git config --global user.name "tu nombre"
git config --global user.email 'tu_email@example.com'
git config --global core.editor emacs
```

4. listar configuración
```bash
git config --list
```

5. ver la configuración de una propiedad especifica
```bash
git config user.name
```

6. crear clave de acceso: a partir del 13 de agosto de 2021, GitHub ya no aceptará contraseñas de cuentas al autenticar operaciones de Git. En su lugar, debe agregar un PAT (*Token de acceso personal*). siga los siguientes pasos método siguiente para agregar un PAT:

    Desde su cuenta de GitHub, vaya a Configuración → Configuración de desarrollador → Token de acceso personal → Generar nuevo token (proporcione su contraseña) → Complete el formulario → haga clic en Generar token → Copie el token generado, será algo así como


7. configurar autenticación
```bash=
# 7.1 generar certificado | linux y mac
ssh-keygen -o -t rsa

# 7.2 mostrar el contenido del archivo generado
cat ruta/id_rsa.pub 

# para windows, mirar este tutorial
# https://phoenixnap.com/kb/generate-ssh-key-windows-10

type ruta/id_rsa.pub # cat en windows

# 7.3 copiar el valor mostrado, ir al repositorio > imagen perfil > configuración > Claves SSH y GPG (SSH and GPG keys) y crear uno nuevo y pegar los valores
```

NOTA: despues de este punto, si es primera vez, intente clonar nuevamente el repositotiorio.


8. clonar repositoporio
```bash
git clone [REPO_URL]
```

9. listar ramas
```bash 
git branch
# o
git branch --list
```

Nota: cuando veas `*` significa que es la rama actual donde estas ubicado



10. cambiar de ramas
```bash=
git checkout [NOMBRE_RAMA]
```

11. creando ramas
```bash
git branch [NOMBRE_RAMA]

# alternativa (*) 
git checkout -b [NOMBRE_RAMA]
```

Nota: se recomienda usar la forma que tiene el `*` ya que crea la rama y se situa en ella


12. ver archivos modificados
```bash
git status
```

13. ver los nuevos cambios
```bash
git diff [archivo]
```

14. devolver un archivo a su estado original
```bash 
git restore [archivo]
```

15. agregar archivos a la rama
```bash 
# agregar uno o varios archivos 
git add archivo [archivo2 archivo n]

# agregar todos los cambios
git add .

# o
git add -A
```

16. confirmar cambios 
```bash
git commit -m "mensaje"
```

17. subir ramas
```bash
git push origin [NOMBRE_RAMA]
```

18. bajar(traer cambios) cambios de una rama
```bash
# principales
git pull [NOMBRE_RAMA]

# secundarias
git pull origin [NOMBRE_RAMA]

# otra forma
git fetch
```

19. merge, consiste en fusionar una rama cualquiera con otra (*la que estas trabajando, por ejemplo*), para hacer esto debes realizar lo siguiente:
```bash
# 1. te ubicas en la rama
git checkout [RAMA_A_FUSIONAR]

# 2. la actualizas
git pull origin [RAMA_A_FUSIONAR]

# 3.te revuelves a tu rama
git merge [RAMA_A_FUSIONAR]
```


20. git revert: a veces, necesitaremos deshacer los cambios que hemos hecho. Hay varias maneras para deshacer nuestros cambios en local y/o en remoto (*dependiendo de lo que necesitemos*), pero necesitaremos utilizar cuidadosamente estos comandos para evitar borrados no deseados.

```bash 
# 1. listar los commits
git log

# o
git log --oneline 


# 2. revertir el cambio
git revert [COMMIT-ID]
```

20. borrar rama

```bash
git branch -d [NOMBRE_RAMA] 
```


## **RECURSOS ADICIONALES**


* [CURSO GIT 1 HORA](https://www.youtube.com/watch?v=VdGzPZ31ts8&ab_channel=HolaMundo)
* [GIT VSCODE](https://www.youtube.com/watch?v=AYbgqmyg7dk&ab_channel=EDteam)
* [GIT DESCKTOP](https://www.youtube.com/watch?v=TuOQBfhp-r0&t=7s&ab_channel=FaztCode)
* [CURSO PASO A PASO](https://www.youtube.com/watch?v=mCVQgSyjCkI&list=PLQxX2eiEaqby-qh4raiKfYyb4T7WyHsfW&ab_channel=TodoCode)
