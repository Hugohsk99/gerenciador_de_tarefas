import tkinter as tk
from tkinter import messagebox
import sqlite3
from login_window import LoginWindow  # Importe a classe LoginWindow


class TaskManager(tk.Tk):
    
    def __init__(self):
        super().__init__()

        self.title("Gerenciador de Tarefas")
        self.geometry("400x400")

        self.tasks = []

        self.tasks_listbox = tk.Listbox(self, selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.add_task_entry = tk.Entry(self)
        self.add_task_entry.pack(pady=10, padx=10, fill=tk.X)

        self.add_task_button = tk.Button(self, text="Adicionar Tarefa", command=self.add_task)
        self.add_task_button.pack(pady=5, padx=10)

        self.edit_task_button = tk.Button(self, text="Editar Tarefa", command=self.edit_task)
        self.edit_task_button.pack(pady=5, padx=10)

        self.delete_task_button = tk.Button(self, text="Excluir Tarefa", command=self.delete_task)
        self.delete_task_button.pack(pady=5, padx=10)

        self.mark_complete_button = tk.Button(self, text="Marcar como Concluída", command=self.mark_complete)
        self.mark_complete_button.pack(pady=5, padx=10)

        self.conn = sqlite3.connect('tasks.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute('CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY, task TEXT)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')

        self.load_tasks()

    def load_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        self.cursor.execute('SELECT * FROM tarefas')
        tasks = self.cursor.fetchall()
        for task in tasks:
            self.tasks.append(task[1])
            self.tasks_listbox.insert(tk.END, task[1])

    def add_task(self):
        task_name = self.add_task_entry.get()
        if task_name:
            self.cursor.execute('INSERT INTO tarefas (task) VALUES (?)', (task_name,))
            self.conn.commit()
            self.tasks.append(task_name)
            self.tasks_listbox.insert(tk.END, task_name)
            self.add_task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Por favor, insira uma tarefa.")

    def edit_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            task_name = self.tasks_listbox.get(selected_task_index)
            new_task_name = self.add_task_entry.get()
            if new_task_name:
                task_id = self.get_task_id(task_name)
                self.cursor.execute('UPDATE tarefas SET task=? WHERE id=?', (new_task_name, task_id))
                self.conn.commit()
                self.tasks_listbox.delete(selected_task_index)
                self.tasks_listbox.insert(selected_task_index, new_task_name)
                self.tasks[selected_task_index[0]] = new_task_name
                self.add_task
    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            task_name = self.tasks_listbox.get(selected_task_index)
            task_id = self.get_task_id(task_name)
            self.cursor.execute('DELETE FROM tarefas WHERE id=?', (task_id,))
            self.conn.commit()
            self.tasks_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index[0]]
        else:
            messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para excluir.")

    def mark_complete(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            task_name = self.tasks_listbox.get(selected_task_index)
            task_id = self.get_task_id(task_name)
            new_task_name = f"{task_name} (Concluída)"
            self.cursor.execute('UPDATE tarefas SET task=? WHERE id=?', (new_task_name, task_id))
            self.conn.commit()
            self.tasks_listbox.delete(selected_task_index)
            self.tasks_listbox.insert(selected_task_index, new_task_name)
            self.tasks[selected_task_index[0]] = new_task_name
        else:
            messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para marcar como concluída.")

    def get_task_id(self, task_name):
        self.cursor.execute('SELECT id FROM tarefas WHERE task=?', (task_name,))
        task_id = self.cursor.fetchone()
        return task_id[0]

    def on_closing(self):
        self.conn.close()
        self.destroy()
    
    def validate_login(self, username, password):
        self.cursor.execute("SELECT * FROM usuarios WHERE username=? AND password=?", (username, password))
        user = self.cursor.fetchone()
        return bool(user)

    def register_user(self, username, password):
        try:
            self.cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
        
def show_login():
    login_window = LoginWindow()
    login_window.protocol("WM_DELETE_WINDOW", login_window.on_closing)
    login_window.mainloop()

if __name__ == "__main__":
    show_login()
