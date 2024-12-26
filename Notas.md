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
    - 