import sqlite3

conexao = sqlite3.connect('DB.db')
print("Conexao Feita")

cursor = conexao.cursor()

cursor.execute("SELECT * FROM funcionarios")
print(cursor.fetchall())