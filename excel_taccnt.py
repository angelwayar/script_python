import pandas as pd
from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("<<Cadena de CNX>>")
db = client["Test"]
collection = db["<<Colección>>"]

# Leer el archivo Excel
df = pd.read_excel("<<Excel>>")

# Convertir el DataFrame de pandas a una lista de diccionarios
data = df.to_dict(orient="records")

# Insertar los datos en la colección de MongoDB
collection.insert_many(data)

print("Datos insertados correctamente en MongoDB.")
