import tkinter as tk
from tkinter import messagebox

class RegisterWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.title("Cadastro")
        self.geometry("300x200")

        self.username_label = tk.Label(self, text="Usuário:")
        self.username_label.pack(pady=10)

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Senha:")
        self.password_label.pack(pady=10)

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.register_button = tk.Button(self, text="Cadastrar", command=self.register)
        self.register_button.pack(pady=10)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.parent.register_user(username, password):
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            self.parent.register_and_login(username, password)  # Registra e faz login automaticamente
            self.destroy()
        else:
            messagebox.showerror("Erro", "Não foi possível cadastrar o usuário")