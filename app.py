import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        self.tasks = []

        # Entrada de nova tarefa
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        # Botões
        tk.Button(root, text="Adicionar Tarefa", command=self.add_task).pack()
        tk.Button(root, text="Remover Selecionada", command=self.remove_task).pack()
        tk.Button(root, text="Marcar como Concluída", command=self.complete_task).pack()

        # Lista de tarefas
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"text": task, "done": False})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Aviso", "Digite uma tarefa!")

    def remove_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.tasks.pop(selected[0])
            self.update_listbox()
            self.save_tasks()

    def complete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            self.update_listbox()
            self.save_tasks()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            text = task["text"]
            if task["done"]:
                text += " ✔"
            self.task_listbox.insert(tk.END, text)

    def save_tasks(self):
        with open(FILE_NAME, "w") as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as f:
                self.tasks = json.load(f)
            self.update_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
