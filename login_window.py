import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from register_window import RegisterWindow
import sqlite3

class LoginWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Login")
        self.attributes('-zoomed', True)  

        self.bind('<Configure>', self.resize)

        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill='both', expand=True)

        style = ttk.Style()
        style.configure("TLabel", foreground="white", background="#123456", font=("Helvetica", 16))  # Tons de azul e preto
        style.configure("TButton", foreground="white", background="#123456", font=("Helvetica", 16))
        style.configure("TEntry", foreground="black", background="white", font=("Helvetica", 16))

        self.username_label = ttk.Label(self.canvas, text="Usuário:")
        self.username_label.place(relx=0.5, rely=0.4, anchor='center')

        self.username_entry = ttk.Entry(self.canvas)
        self.username_entry.place(relx=0.5, rely=0.45, anchor='center')

        self.password_label = ttk.Label(self.canvas, text="Senha:")
        self.password_label.place(relx=0.5, rely=0.55, anchor='center')

        self.password_entry = ttk.Entry(self.canvas, show="*")
        self.password_entry.place(relx=0.5, rely=0.6, anchor='center')

        self.login_button = ttk.Button(self.canvas, text="Login", command=self.login)
        self.login_button.place(relx=0.5, rely=0.7, anchor='center')

        self.register_button = ttk.Button(self.canvas, text="Cadastrar", command=self.open_register_window)
        self.register_button.place(relx=0.5, rely=0.75, anchor='center')

        self.load_bg_image()

    def load_bg_image(self):
        # Carregue a imagem de fundo com PIL e converta para PhotoImage
        image = Image.open("imagens/12706.jpg")  # Substitua com o caminho da sua imagem
        image = image.resize((self.winfo_screenwidth(), self.winfo_screenheight()), Image.ANTIALIAS)  # Redimensiona a imagem para caber na janela
        self.bg_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor='nw')

    def resize(self, event):  # Função para ajustar os widgets
        self.load_bg_image()

    # Resto do código...

    
    def register_user(self, username, password):
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.validate_login(username, password):
            self.destroy()
            from gerenciador_tarefas import TaskManager  # Importe a classe TaskManager aqui
            gerenciador_tarefas = TaskManager()
            gerenciador_tarefas.protocol("WM_DELETE_WINDOW", gerenciador_tarefas.on_closing)
            gerenciador_tarefas.mainloop()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos")
    
    

    def validate_login(self, username, password):
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()
        return bool(user)
    
    def register_and_login(self, username, password):
        self.destroy()
        gerenciador_tarefas = TaskManager()
        gerenciador_tarefas.protocol("WM_DELETE_WINDOW", gerenciador_tarefas.on_closing)
        gerenciador_tarefas.mainloop()

    def open_register_window(self):
        RegisterWindow(self)  # Pass 'self' instead of 'self.parent'
    
    def on_closing(self):
        self.destroy()

