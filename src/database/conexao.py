import os

import mysql.connector
from dotenv import load_dotenv


load_dotenv()


def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="1234",
        database="techservice_db"
    )
    return conexao

 
