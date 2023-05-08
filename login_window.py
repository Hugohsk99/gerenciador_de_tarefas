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

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.validate_login(username, password):
            self.destroy()
            from task_manager import TaskManager  # Importe a classe TaskManager aqui
            task_manager = TaskManager()
            task_manager.protocol("WM_DELETE_WINDOW", task_manager.on_closing)
            task_manager.mainloop()
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
        task_manager = TaskManager()
        task_manager.protocol("WM_DELETE_WINDOW", task_manager.on_closing)
        task_manager.mainloop()

    def open_register_window(self):
        RegisterWindow(self.parent)
    
    def on_closing(self):
        self.destroy()

