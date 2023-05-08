import tkinter as tk
from tkinter import messagebox

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

    def add_task(self):
        task_name = self.add_task_entry.get()
        if task_name:
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
                self.tasks_listbox.delete(selected_task_index)
                self.tasks_listbox.insert(selected_task_index, new_task_name)
                self.tasks[selected_task_index[0]] = new_task_name
                self.add_task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Aviso", "Por favor, insira uma tarefa.")
        else:
            messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para editar.")

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            self.tasks_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index[0]]
        else:
            messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para excluir.")

    def mark_complete(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            task_name = self.tasks_listbox.get(selected_task_index)
            self.tasks_listbox.delete(selected_task_index)
            self.tasks_listbox.insert(selected_task_index, f"{task_name} (Concluída)")
            self.tasks[selected_task_index[0]] = f"{task_name} (Concluída)"
        else:
            messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para marcar como concluída.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.mainloop()
