import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk  # Importe Image e ImageTk de PIL
from register_window import RegisterWindow
import sqlite3

class LoginWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Login")
        self.attributes('-zoomed', True)  # Maximiza a janela mantendo a barra de ações

        self.bind('<Configure>', self.resize)  # Vincular evento de redimensionamento

        # Crie um canvas e desenhe a imagem de fundo
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill='both', expand=True)

        # Crie um frame para conter os widgets
        frame = ttk.Frame(self.canvas)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        # Cria um estilo
        style = ttk.Style()
        style.configure("TLabel", foreground="white", background="#123456", font=("Helvetica", 12))
        style.configure("TButton", foreground="white", background="#123456", font=("Helvetica", 12))
        style.configure("TEntry", foreground="black", background="white", font=("Helvetica", 12))

        self.username_label = ttk.Label(frame, text="Usuário:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)

        self.username_entry = ttk.Entry(frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_label = ttk.Label(frame, text="Senha:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10)

        self.password_entry = ttk.Entry(frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.login_button = ttk.Button(frame, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        self.register_button = ttk.Button(frame, text="Cadastrar", command=self.open_register_window)
        self.register_button.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

        # Load background image initially
        self.load_bg_image()

    def load_bg_image(self):
        # Carregue a imagem de fundo com PIL e converta para PhotoImage
        image = Image.open("12706.jpg")  # Substitua com o caminho da sua imagem
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

