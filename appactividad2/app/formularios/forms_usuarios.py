import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class FormUsuarios(tk.Tk):
    def __init__(self, parent):
        self.tipo_action = "Guardar"
        self.tipo_user = ""
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(self.frame, text="Registro de usuarios", font=('Times', 16)).place(x=70, y=30)

        labelcedula = tk.Label(self.frame, text="id", font=('Times', 14))
        labelcedula.place(x=70, y=100)
        self.ccedula = tk.Entry(self.frame, width=40)
        self.ccedula.place(x=220, y=100)

        labelnombre = tk.Label(self.frame, text="Nombre", font=('Times', 14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame, width=40)
        self.cnombre.place(x=220, y=130)

        labelusuario = tk.Label(self.frame, text="Username", font=('Times', 14))
        labelusuario.place(x=70, y=160)
        self.cusuario = tk.Entry(self.frame, width=40)
        self.cusuario.place(x=220, y=160)

        labelcontrasena = tk.Label(self.frame, text="Contraseña", font=('Times', 14))
        labelcontrasena.place(x=500, y=100)
        self.ccontrasena = tk.Entry(self.frame, width=40, show="*")
        self.ccontrasena.place(x=600, y=100)

        labelcorreo = tk.Label(self.frame, text="Correo", font=('Times', 14))
        labelcorreo.place(x=500, y=130)
        self.ccorreo = tk.Entry(self.frame, width=40)
        self.ccorreo.place(x=600, y=130)

        labeltipo = tk.Label(self.frame, text="Rol", font=('Times', 14))
        labeltipo.place(x=500, y=160)
        self.ctipo = ttk.Combobox(self.frame, width=40, state="readonly")
        self.ctipo.place(x=600, y=160)
        self.ctipo["values"] = ("Administrador", "Vendedor")

        btn_guardar = tk.Button(self.frame, text="Guardar", font=('Times', 14), width=10, command=self.guardar_usuario)
        btn_guardar.place(x=70, y=190)

        btn_eliminar = tk.Button(self.frame, text="Eliminar", font=('Times', 14), width=10, command=self.Eliminar_usuario)
        btn_eliminar.place(x=180, y=190)

        btn_actualizar = tk.Button(self.frame, text="Actualizar", font=('Times', 14), width=10, command=self.Actualizar_usuario)
        btn_actualizar.place(x=290, y=190)

        self.listar_usuarios()

    def guardar_usuario(self):
        if not self.validar_campos():
            messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos")
            return

        new_user = {
            "id": self.ccedula.get(),
            "name": self.cnombre.get(),
            "username": self.cusuario.get(),
            "password": self.ccontrasena.get(),
            "email": self.ccorreo.get(),
            "role": self.ctipo.get()
        }

        with open(r"C:\\Users\\DIEGO YEPES\\Desktop\\appactividad2\\app\\db_users.json", "r+", encoding="utf-8") as file:
            data = json.load(file)
            data["users"].append(new_user)
            file.seek(0)
            json.dump(data, file, indent=4)

        self.tablausuarios.insert("", "end", text=new_user["id"], values=(new_user["name"], new_user["username"], new_user["email"], new_user["role"]))
        self.limpiar_campos()
        messagebox.showinfo("Información", "USUARIO GUARDADO")

    def Eliminar_usuario(self):
        if not self.tablausuarios.selection():
            messagebox.showwarning("Advertencia", "Seleccione un usuario para eliminar")
            return

        if not messagebox.askyesno("Confirmación", "¿Está seguro de que desea eliminar este usuario?"):
            return

        selected_item = self.tablausuarios.selection()[0]
        user_id = self.tablausuarios.item(selected_item, "text")

        with open(r"C:\\Users\\DIEGO YEPES\\Desktop\\appactividad2\\app\\db_users.json", "r+", encoding="utf-8") as file:
            data = json.load(file)
            data["users"] = [user for user in data["users"] if user["id"] != user_id]
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=4)

        self.tablausuarios.delete(selected_item)
        messagebox.showinfo("Información", "USUARIO ELIMINADO")

    def Actualizar_usuario(self):
        if not self.validar_campos():
            messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos")
            return

        if not self.tablausuarios.selection():
            messagebox.showwarning("Advertencia", "Seleccione un usuario para actualizar")
            return

        if not messagebox.askyesno("Confirmación", "¿Está seguro de que desea actualizar este usuario?"):
            return

        selected_item = self.tablausuarios.selection()[0]
        user_id = self.tablausuarios.item(selected_item, "text")

        updated_user = {
            "id": self.ccedula.get(),
            "name": self.cnombre.get(),
            "username": self.cusuario.get(),
            "password": self.ccontrasena.get(),
            "email": self.ccorreo.get(),
            "role": self.ctipo.get()
        }

        with open(r"C:\\Users\\DIEGO YEPES\\Desktop\\appactividad2\\app\\db_users.json", "r+", encoding="utf-8") as file:
            data = json.load(file)
            for i, user in enumerate(data["users"]):
                if user["id"] == user_id:
                    data["users"][i] = updated_user
                    break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=4)

        self.tablausuarios.item(selected_item, text=updated_user["id"], values=(updated_user["name"], updated_user["username"], updated_user["email"], updated_user["role"]))
        self.limpiar_campos()
        messagebox.showinfo("Información", "USUARIO ACTUALIZADO")

    def listar_usuarios(self):
        tk.Label(self.frame, text="Listado de usuarios", font=('Times', 16)).place(x=70, y=230)

        self.tablausuarios = ttk.Treeview(self.frame, columns=("nombre", "usuario", "correo", "rol"))
        self.tablausuarios.heading("#0", text="id")
        self.tablausuarios.heading("nombre", text="Nombre")
        self.tablausuarios.heading("usuario", text="Usuario")
        self.tablausuarios.heading("correo", text="Correo")
        self.tablausuarios.heading("rol", text="Rol")
        self.tablausuarios.place(x=70, y=280)

        self.tablausuarios.bind("<<TreeviewSelect>>", self.rellenar_campos)
        self.tablausuarios.bind("<Button-1>", self.deseleccionar)

        with open(r"C:\\Users\\DIEGO YEPES\\Desktop\\appactividad2\\app\\db_users.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            for user in data["users"]:
                self.tablausuarios.insert("", "end", text=user["id"], values=(user["name"], user["username"], user["email"], user["role"]))

    def rellenar_campos(self, _):
        if not self.tablausuarios.selection():
            self.limpiar_campos()
            return

        selected_item = self.tablausuarios.selection()[0]
        user_id = self.tablausuarios.item(selected_item, "text")

        with open(r"C:\\Users\\DIEGO YEPES\\Desktop\\appactividad2\\app\\db_users.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            user = next((user for user in data["users"] if user["id"] == user_id), None)
            if user:
                self.ccedula.delete(0, tk.END)
                self.ccedula.insert(0, user["id"])
                self.cnombre.delete(0, tk.END)
                self.cnombre.insert(0, user["name"])
                self.cusuario.delete(0, tk.END)
                self.cusuario.insert(0, user["username"])
                self.ccontrasena.delete(0, tk.END)
                self.ccontrasena.insert(0, user["password"])
                self.ccorreo.delete(0, tk.END)
                self.ccorreo.insert(0, user["email"])
                self.ctipo.set(user["role"])

    def deseleccionar(self, event):
        if self.tablausuarios.identify_region(event.x, event.y) == "nothing":
            self.tablausuarios.selection_remove(self.tablausuarios.selection())

    def limpiar_campos(self):
        self.ccedula.delete(0, tk.END)
        self.cnombre.delete(0, tk.END)
        self.cusuario.delete(0, tk.END)
        self.ccontrasena.delete(0, tk.END)
        self.ccorreo.delete(0, tk.END)
        self.ctipo.set("")

    def validar_campos(self):
        return all([
            self.ccedula.get(),
            self.cnombre.get(),
            self.cusuario.get(),
            self.ccontrasena.get(),
            self.ccorreo.get(),
            self.ctipo.get()
        ])
