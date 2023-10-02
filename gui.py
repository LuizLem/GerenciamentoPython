import sqlite3
import os
import tkinter 
from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import ImageTk, Image

conexao = sqlite3.connect('DB.db')
print("Conexao Feita")

cursor = conexao.cursor()

def criar_nova_janela():
    nova_janela = tkinter.Toplevel()
    nova_janela.title("Central")
    nova_janela.geometry("350x140")
    titulo_label = ttk.Label(master=nova_janela, text="Central da Padaria da Vila", font=('Century Gotich', 16))
    titulo_label.pack(pady=20)
    botao_funcionarios = customtkinter.CTkButton(master=nova_janela, text="Funcionários", font=("Century Gotich", 12), corner_radius=6, command=lambda: os.system('funcionarios.py'))
    botao_funcionarios.place(x=20,y=90)
    botao_produtos = customtkinter.CTkButton(master=nova_janela, text="Produtos", font=("Century Gotich", 12), corner_radius=6, command=lambda: os.system('produtos.py'))
    botao_produtos.place(x=190,y=90)
    nova_janela.iconbitmap("logoo.ico")
    nova_janela.mainloop()

def logar():
    username = login1.get()
    password = senha2.get()
    conn = sqlite3.connect('DB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM login WHERE usuario=? AND senha=?', (username, password))
    resultado = cursor.fetchone()
    if resultado:
        print("OK")
        tkinter.messagebox.showinfo("Sucesso", "Seja Bem-Vindo Administrador!")
        criar_nova_janela()
    else:
        tkinter.messagebox.showerror("Erro no login", "Credenciais Invalidas ou Inexistentes")
        print("NO OK")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app=customtkinter.CTk()
app.geometry("350x400")
app.resizable(0,0)
app.title('Padaria da Vila')
app.iconbitmap("logoo.ico")
img2 = (Image.open("vila.png"))
resized_image = img2.resize((350,45))
new_image = ImageTk.PhotoImage(resized_image)
label = Label(app, image = new_image)
label.pack()

img1=ImageTk.PhotoImage(Image.open("pattern.png"))
l1=customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2=customtkinter.CTkLabel(master=frame, text="Entre com suas credenciais", font=('Century Gotich', 20))
l2.place(x=43, y=45)

login1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Usuário")
login1.place(x=50,y=110)

senha2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Senha")
senha2.place(x=50,y=165)

botaologin=customtkinter.CTkButton(master=frame, width=220, text='Entrar', corner_radius=6, command=logar)
botaologin.place(x=50,y=240)


app.mainloop()