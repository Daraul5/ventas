import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Proveedor(tk.Frame):

    def __init__(self, padre):
        super().__init__(padre)
        self.con = sqlite3.connect('database.db')
        self.cur = self.con.cursor()
        self.lista_proveedores = []
        self.widgets()
        self.cargar_proveedores() # Cargar los proveedores al inicio

    def widgets(self):
        labelframetree = tk.LabelFrame(self, text="Proveedores", font="Arial 14 bold", bg="#95c799")
        labelframetree.place(x=300, y=10, width=780, height=580)

        scroly= ttk.Scrollbar(labelframetree)
        scroly.pack(side=RIGHT, fill=Y)

        scrolx = ttk.Scrollbar(labelframetree, orient=HORIZONTAL)
        scrolx.pack(side=BOTTOM, fill=X)

        self.treeproveedores = ttk.Treeview(labelframetree, yscrollcommand=scroly.set, xscrollcommand=scrolx.set, height=40,
                                            columns=("ID", "Nombre", "Telefono", "Email", "Fecha"), show="headings")
        self.treeproveedores.pack(expand=True, fill=BOTH)

        scrolx.config(command=self.treeproveedores.xview)
        scroly.config(command=self.treeproveedores.yview)

        self.treeproveedores.heading("ID", text="ID")
        self.treeproveedores.heading("Nombre", text="Nombre")
        self.treeproveedores.heading("Telefono", text="Telefono")
        self.treeproveedores.heading("Email", text="Email")
        self.treeproveedores.heading("Fecha", text="Fecha")

        self.treeproveedores.column("ID", width=50, anchor="center")
        self.treeproveedores.column("Nombre", width=200, anchor="center")
        self.treeproveedores.column("Telefono", width=100, anchor="center")
        self.treeproveedores.column("Email", width=200, anchor="center")
        self.treeproveedores.column("Fecha", width=100, anchor="center")

        lableframellenar = tk.LabelFrame(self, text="Llenar Datos", font="Arial 14 bold", bg="#95c799")
        lableframellenar.place(x=10, y=10, width=280, height=580)

        tk.Label(lableframellenar, text="Nombre", font="arial 12 bold", bg="#95c799").place(x=10, y=10)
        self.entry_nombre = ttk.Entry(lableframellenar, font="arial 12 bold")
        self.entry_nombre.place(x=10, y=40, width=250, height=40)

        tk.Label(lableframellenar, text="Numero", font="arial 12 bold", bg="#95c799").place(x=10, y=80)
        self.entry_numero = ttk.Entry(lableframellenar, font="arial 12 bold")
        self.entry_numero.place(x=10, y=110, width=250, height=40)

        tk.Label(lableframellenar, text="Email", font="arial 12 bold", bg="#95c799").place(x=10, y=150)
        self.entry_email = ttk.Entry(lableframellenar, font="arial 12 bold")
        self.entry_email.place(x=10, y=180, width=250, height=40)

        tk.Label(lableframellenar, text="Fecha", font="arial 12 bold", bg="#95c799").place(x=10, y=220)
        self.entry_fecha = ttk.Entry(lableframellenar, font="arial 12 bold")
        self.entry_fecha.place(x=10, y=250, width=250, height=40)
        self.entry_fecha.insert(0, "dd/mm/aaaa")
        self.entry_fecha.bind("<FocusIn>", lambda e: self.entry_fecha.delete(0, tk.END))
        self.entry_fecha.bind("<FocusOut>", lambda e: self.entry_fecha.insert(0, "dd/mm/aaaa") if self.entry_fecha.get() == "" else None)

        btn_agregar = tk.Button(lableframellenar, text="Agregar", font="arial 12 bold", bg="white", command=self.agregar_proveedor)
        btn_agregar.place(x=10, y=350, width=250, height=40)

        btn_editar = tk.Button(lableframellenar, text="Editar", font="arial 12 bold", bg="white")
        btn_editar.place(x=10, y=400, width=250, height=40)

        btn_eliminar = tk.Button(lableframellenar, text="Eliminar", font="arial 12 bold", bg="white")
        btn_eliminar.place(x=10, y=450, width=250, height=40)

    def cargar_proveedores(self):
        try:
            self.cur.execute("SELECT id, nombre, telefono, email, fecha FROM proveedores")
            proveedores = self.cur.fetchall()
            self.actualizar_lista_proveedores_desde_db(proveedores)
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al cargar proveedores: {e}")

    def actualizar_lista_proveedores_desde_db(self, proveedores):
        for widget in self.treeproveedores.get_children():
            self.treeproveedores.delete(widget)

        for proveedor in proveedores:
            self.treeproveedores.insert("", "end", values=(proveedor[0], proveedor[1], proveedor[2], proveedor[3], proveedor[4]))

    def agregar_proveedor(self):
        nombre = self.entry_nombre.get()
        numero = self.entry_numero.get()
        email = self.entry_email.get()
        fecha = self.entry_fecha.get()

        if not nombre or not numero or not email or not fecha:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            self.cur.execute("INSERT INTO proveedores (nombre, telefono, email, fecha) VALUES (?, ?, ?, ?)", (nombre, numero, email, fecha))
            self.con.commit()
            messagebox.showinfo("Éxito", "Proveedor agregado correctamente")
            self.cargar_proveedores() # Recargar la lista de proveedores desde la base de datos
            
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al agregar proveedor: {e}")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Gestión de Proveedores")
    root.geometry("1100x600+100+50")
    root.config(bg="#f0f0f0")
    app = Proveedor(root)
    app.pack(expand=True, fill=BOTH)
    root.mainloop()
        
        
        
        
        
        