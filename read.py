import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('facturas.db')
cursor = conn.cursor()

# Ejecutar una consulta
cursor.execute("SELECT * FROM facturas")
rows = cursor.fetchall()

# Mostrar los resultados
for row in rows:
    print(row)

# Cerrar la conexión
conn.close()