from flask import Flask, render_template, request, redirect
from supabase import create_client, Client
from dotenv import load_dotenv 
import os

# Configurar Flask
app = Flask(__name__)

load_dotenv()

# Configurar Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")  # Reemplaza con tu URL
SUPABASE_KEY = os.getenv("SUPABASE_KEY")  # Reemplaza con tu clave "anon"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Ruta principal con formulario
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para insertar datos
@app.route('/insert', methods=['POST'])
def insert_data():
    name = request.form['name']
    email = request.form['email']

    # Insertar datos en Supabase
    data = {"name": name, "email": email}
    response = supabase.table("users").insert(data).execute()

    # Comprobar si hay datos en la respuesta
    if response.data:
        return f"<h1>Datos enviados exitosamente</h1><p>{response.data}</p><a href='/'>Regresar</a>"
    elif response.error_message:
        return f"<h1>Error al enviar datos</h1><p>{response.error_message}</p><a href='/'>Regresar</a>"
    elif response.errors:
        return f"<h1>Error al enviar datos</h1><p>{response.errors}</p><a href='/'>Regresar</a>"
    else:
        return "<h1>Respuesta inesperada del servidor.</h1><a href='/'>Regresar</a>"

# Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True)
