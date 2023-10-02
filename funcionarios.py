import tkinter as tk
import sqlite3
from tkinter import ttk

def mostrar_funcionarios():
    conn = sqlite3.connect('DB.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome, funcao, salario FROM funcionarios")
    resultados = cursor.fetchall()

    for i in tree.get_children():
        tree.delete(i)

    for resultado in resultados:
        tree.insert('', 'end', values=resultado)

    conn.close()

def adicionar_funcionario():
    novo_id = id_novo_entry.get()
    novo_nome = nome_novo_entry.get()
    nova_funcao = funcao_novo_entry.get()
    novo_salario = salario_novo_entry.get()

    conn = sqlite3.connect('DB.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO funcionarios (id, nome, funcao, salario) VALUES (?, ?, ?, ?)",
                   (novo_id, novo_nome, nova_funcao, novo_salario))
    conn.commit()

    conn.close()
    mostrar_funcionarios()

def alterar_funcionario():
    id_para_alterar = id_alterar_entry.get()
    novo_id = novo_id_entry.get()
    novo_nome = novo_nome_entry.get()
    nova_funcao = nova_funcao_entry.get()
    novo_salario = novo_salario_entry.get()

    conn = sqlite3.connect('DB.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE funcionarios SET id=?, nome=?, funcao=?, salario=? WHERE id=?",
                   (novo_id, novo_nome, nova_funcao, novo_salario, id_para_alterar))
    conn.commit()

    conn.close()
    mostrar_funcionarios() 

def apagar_id():
    id_a_apagar = id_apagar_entry.get()

    conn = sqlite3.connect('DB.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM funcionarios WHERE id=?", (id_a_apagar,))
    conn.commit()

    conn.close()
    mostrar_funcionarios() 

janela = tk.Tk()
janela.title("Central dos Funcionarios")
janela.iconbitmap("logoo.ico")

mostrar_button = tk.Button(janela, text="Mostrar Funcionários", command=mostrar_funcionarios)
mostrar_button.pack()

tree = ttk.Treeview(janela, columns=("ID", "Nome", "Função", "Salário"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Função", text="Função")
tree.heading("Salário", text="Salário")
tree.pack()

id_novo_label = tk.Label(janela, text="Novo ID:")
id_novo_label.pack()
id_novo_entry = tk.Entry(janela)
id_novo_entry.pack()

nome_novo_label = tk.Label(janela, text="Novo Nome:")
nome_novo_label.pack()
nome_novo_entry = tk.Entry(janela)
nome_novo_entry.pack()

funcao_novo_label = tk.Label(janela, text="Nova Função:")
funcao_novo_label.pack()
funcao_novo_entry = tk.Entry(janela)
funcao_novo_entry.pack()

salario_novo_label = tk.Label(janela, text="Novo Salário:")
salario_novo_label.pack()
salario_novo_entry = tk.Entry(janela)
salario_novo_entry.pack()

adicionar_button = tk.Button(janela, text="Adicionar Funcionário", command=adicionar_funcionario)
adicionar_button.pack()

id_alterar_label = tk.Label(janela, text="ID do Funcionário para Alterar:")
id_alterar_label.pack()
id_alterar_entry = tk.Entry(janela)
id_alterar_entry.pack()

novo_id_label = tk.Label(janela, text="Novo ID:")
novo_id_label.pack()
novo_id_entry = tk.Entry(janela)
novo_id_entry.pack()

novo_nome_label = tk.Label(janela, text="Novo Nome:")
novo_nome_label.pack()
novo_nome_entry = tk.Entry(janela)
novo_nome_entry.pack()

nova_funcao_label = tk.Label(janela, text="Nova Função:")
nova_funcao_label.pack()
nova_funcao_entry = tk.Entry(janela)
nova_funcao_entry.pack()

novo_salario_label = tk.Label(janela, text="Novo Salário:")
novo_salario_label.pack()
novo_salario_entry = tk.Entry(janela)
novo_salario_entry.pack()

alterar_button = tk.Button(janela, text="Alterar Funcionário", command=alterar_funcionario)
alterar_button.pack()

id_apagar_label = tk.Label(janela, text="ID do Funcionário para Apagar:")
id_apagar_label.pack()
id_apagar_entry = tk.Entry(janela)
id_apagar_entry.pack()

apagar_button = tk.Button(janela, text="Apagar ID", command=apagar_id)
apagar_button.pack()

janela.mainloop()
