1. Instalar git bash
2. En git bash crear carpeta para el proyecto
3. Instalar entorno virtual con git bash desde terminal de VSC:
    a. crear entorno: python -m venv dataanalyst
    b. activar entorno: source dataanalyst/Scripts/activate

Nota: ojo, el comando "source" es cuando se hace desde git bash

4. Crear proyecto en supabase.com "supabase.com".
5. Desde supabase se puede usar el SQL editor para probar la creación de comandos de SQL, como: crear tabla, insertar datos en tabla y consultar tabla. 
6. Instalar librerias necesarias para el proyecto en entorno virtual, desde la terminal de git bash en VSC.
    a. Si pide actualizar pip, correr todo el comando sugerido en consola con comillas dobles al principio y final, así: "C:\Users\ASUS\OneDrive\Data World\Programas\Data Analyst Carreer\app_flask\dataanalyst\Scripts\python.exe" -m pip install --upgrade pip
    b. Instalar librerias necesarias para el proyecto:
        - pip install flask supabase psycopg2
        - Crear dependencias del proyecto: pip freeze > requirements.txt 

    Nota: el comando de dependencias se puede ejecutar muchas veces y se van actualizando las librerias.

7. Crear estructura del proyecto:

mi_proyecto/
│
├── app.py                 # Código principal de Flask
├── requirements.txt       # Dependencias
└── templates/             # Carpeta para plantillas HTML
    └── index.html         # Página HTML para el formulario

8. Crear estructura del proyecto como se ve arriba, con el archivo app.py y templates / index.html que se ven en esta carpeta.
9. Al crear la tabla en "supabase" crearla sin RLS (Row level security) para que no arroje error al momento de insertar datos.
10. Crear varibles de entorno en archivo .env para que no se vean al momento de publicar el archivo.
11. Para que lo anterior suceda, crear el archivo .gitignore y colocar ese archivo que no debe aparecer:
    - .env
12. Crear repositorio de git (para publicar en git hub):
    - git init
    - git add
    - git commit -m "nombre del commit"
    - git branch -M main
    - git remote add origin https://github.com/Elkinrodriguez77/1.1-Crear-base-y-enviar-datos.git (cambiar con la ruta del rep de git hub)
    - git push -u origin main (enviar información al repositorio)

13. Desactivar entorno local:
    - deactivate (en terminal)

14. Conectar la base de supabase a PGAdmin o DBEaber:
    a. Ir a supabase
    b. Ir a Database
    c. Hacer clic en el botón superior de "connect"
    d. Ir a transaction pooler
    e. Desplegar en esa sección lo que dice "View parameters"
    f. Con esos parametros hacer la conexión, la contraseña es la que se asigna a la base al momento de crearla, que se puede reestablecer si se requiere desde "Project Settings"
15. Conectar la base de supabase a power BI, se hace siguiendo los mismos parametros del punto anterior, lo que hay que tener en cuenta, es que en PBI se debe deshabilitar desde la configuración de origen de datos, el "cifrado de datos" de la conexión para que todo funcione de forma adecuada. 

Nota: al parecer el tema de la conexión directa de supabase no funciona por mi Wifi actual en el hotel de canada, es por un tema de la IP que el wifi no soporte. Validar en otra red para ver si funciona de forma adecuada. 



------------ desplegar app en azure -------

1. Crear un grupo de recursos
2. Crear una Wep App
    - Escoger grupo de recursos
    - Colocar nombre a la instancia
    - Escoger "Code" en publish
    - Seleccionar la región
    - En Sección "pricing plans" crear uno nuevo
    - En tipo de pricing, seleecionar el gratuito "Free F1"

3. Crear recurso
4. Ir al recurso creado
5. Cargar app mediante git hub:
    - Deployment center
    - Seleccionar git hub
    - Escoger repositorio
    - De lo demás se encarga azure

Es un proceso muy intutivo.

6. Colocar variables de entorno:
    - Como no cargué el .env, debo colocar las variables de supabase o las requeridas:
        - En Settings > "Enviroment variables"
        - Cargarlas en "+Add" y luego hacer clic en Save