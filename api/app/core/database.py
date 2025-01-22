import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  

dbname = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')

DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

try:
    connection = psycopg2.connect(DATABASE_URL)
    print("Conectado ao banco de dados")
except psycopg2.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")