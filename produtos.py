import tkinter as tk
import sqlite3
from tkinter import ttk
import customtkinter


def mostrar_produtos():
    categoria = categoria_combo.get()
    conn = sqlite3.connect('DB.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT id, nome, preco FROM {categoria}")
    resultados = cursor.fetchall()

    for i in tree.get_children():
        tree.delete(i)

    for resultado in resultados:
        tree.insert('', 'end', values=resultado)

    conn.close()

def apagar_produto():
    categoria = categoria_combo.get()
    id_a_apagar = id_entry.get()
    conn = sqlite3.connect('DB.db')
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM {categoria} WHERE id=?", (id_a_apagar,))
    conn.commit()

    conn.close()
    mostrar_produtos()
def adicionar_produto():
    categoria = categoria_combo.get()
    novo_id = id_novo_entry.get()
    novo_nome = nome_novo_entry.get()
    novo_preco = preco_novo_entry.get()
    
    conn = sqlite3.connect('DB.db')
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO {categoria} (id, nome, preco) VALUES (?, ?, ?)", (novo_id, novo_nome, novo_preco))
    conn.commit()

    conn.close()
    mostrar_produtos()

janela = tk.Tk()
janela.title("Central dos Produtos")
janela.iconbitmap("logoo.ico")

categorias = ['Bebidas', 'BiscoitosSalgadinhos', 'Bolos', 'Doces', 'Paes', 'Salgados', 'SalgadosAssados', 'Sanduiches', 'Sobremesas']
categoria_label = tk.Label(janela, text="Selecione a Categoria:")
categoria_label.pack()
categoria_combo = ttk.Combobox(janela, values=categorias)
categoria_combo.pack()
categoria_combo.set(categorias[0]) 

mostrar_button = tk.Button(janela, text="Mostrar Produtos", command=mostrar_produtos)
mostrar_button.pack()

tree = ttk.Treeview(janela, columns=("ID", "Nome", "Preço"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Preço", text="Preço")
tree.pack()

id_label = tk.Label(janela, text="Digite o ID para apagar:")
id_label.pack()
id_entry = tk.Entry(janela)
id_entry.pack()

apagar_button = tk.Button(janela, text="Apagar", command=apagar_produto)
apagar_button.pack()

id_novo_label = tk.Label(janela, text="ID:")
id_novo_label.pack()
id_novo_entry = tk.Entry(janela)
id_novo_entry.pack()

nome_novo_label = tk.Label(janela, text="Nome:")
nome_novo_label.pack()
nome_novo_entry = tk.Entry(janela)
nome_novo_entry.pack()

preco_novo_label = tk.Label(janela, text="Preço:")
preco_novo_label.pack()
preco_novo_entry = tk.Entry(janela)
preco_novo_entry.pack()

adicionar_button = tk.Button(janela, text="Adicionar Produto", command=adicionar_produto)
adicionar_button.pack()

janela.mainloop()
