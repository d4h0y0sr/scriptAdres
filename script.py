import os
import re
import sqlite3
from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError

# Función para extraer el CUFE usando una expresión regular
def extract_cufe(text):
    cufe_pattern = re.compile(r'\b([0-9a-fA-F]\n*){95,100}\b')
    match = cufe_pattern.search(text)
    if match:        
        return match.group()    
    return None

# Función para obtener el peso del archivo
def get_file_size(file_path):
    return os.path.getsize(file_path)

# Conectar a la base de datos SQLite (se creará si no existe)
conn = sqlite3.connect('facturas.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS facturas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_archivo TEXT,
    numero_paginas INTEGER,
    cufe TEXT,
    peso_archivo INTEGER
)
''')

# Obtener la ruta del directorio del script
script_directory = os.path.dirname(os.path.abspath(__file__))
# Directorio donde se encuentran los archivos PDF
pdf_directory = os.path.join(script_directory, 'facturas')

# Iterar sobre los archivos PDF en el directorio
for filename in os.listdir(pdf_directory):    
    file_path = os.path.join(pdf_directory, filename)
    try:
        # Leer el archivo PDF
        reader = PdfReader(file_path)
        num_pages = len(reader.pages)
        # Extraer texto de todas las páginas
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        
        # Extraer el CUFE
        cufe = extract_cufe(text)
        
        # Obtener el peso del archivo
        file_size = get_file_size(file_path)
        
        # Insertar los datos en la base de datos
        cursor.execute('''
        INSERT INTO facturas (nombre_archivo, numero_paginas, cufe, peso_archivo)
        VALUES (?, ?, ?, ?)
        ''', (filename, num_pages, cufe, file_size))
    except PdfReadError:
            print(f"Error: {filename} no es un archivo PDF válido.")
    except Exception as e:
        print(f"Error inesperado al procesar {filename}: {e}")
# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Proceso completado. Los datos han sido almacenados en la base de datos.")
