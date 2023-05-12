import tkinter as tk
from tkinter import messagebox
from register_window import RegisterWindow
import sqlite3

class LoginWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Login")
        self.geometry("300x200")

        self.username_label = tk.Label(self, text="Usuário:")
        self.username_label.pack(pady=10)

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Senha:")
        self.password_label.pack(pady=10)

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        self.register_button = tk.Button(self, text="Cadastrar", command=self.open_register_window)
        self.register_button.pack()
    
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

