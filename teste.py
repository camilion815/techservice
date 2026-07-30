import mysql.connector
 
try:
    conexao = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="1234",
        database="techservice_db"
    )
 
    if conexao.is_connected():
        print("✅ Conectado!")
 
        cursor = conexao.cursor()
        cursor.execute("SELECT DATABASE();")
 
        print(cursor.fetchone())
 
        cursor.close()
        conexao.close()
 
except Exception as e:
    print("ERRO:")
    print(e)