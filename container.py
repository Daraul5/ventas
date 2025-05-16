from tkinter import *
import tkinter as tk
from ventas import Ventas
from inventario import Inventario
from categorias import Categorias
from pedidos import Pedidos
from proveedor import Proveedor
from informacion import Informacion
from abstracs import ModuleInterface
import sys
import os

class Container(tk.Frame, ModuleInterface):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.place(x=0, y=0, width=1100, height=650)
        self.widgets()
        self.frames = {}

        for i in (Ventas, Inventario, Categorias, Pedidos, Proveedor, Informacion):
            try:
                frame = i(self)
                self.frames[i] = frame
                print(f"Frame {i.__name__} inicializado correctamente: {frame}")  # Depuración
                frame.config(bg="#95c799", highlightbackground="gray", highlightthickness=1)
                frame.place(x=0, y=40, width=1100, height=610)
            except Exception as e:
                print(f"Error al inicializar {i.__name__}: {e}")

        self.show_frames(Proveedor)

    def show_frames(self, container):
        frame = self.frames.get(container)
        if frame:
            print(f"Levantando frame: {container.__name__}")  # Confirmar el frame que se está levantando
            frame.tkraise()
        else:
            print(f"Error: El frame {container.__name__} no está inicializado o fue destruido.")


    def ventas(self):
        self.show_frames(Ventas)

    def inventario(self):
        print("Frames disponibles en self.frames:", self.frames.keys())  # Depuración adicional
        if Inventario in self.frames:
            self.show_frames(Inventario)
        else:
            print("Error: El frame Inventario no está disponible.")

    def categorias(self):
        self.show_frames(Categorias)
        # Asegurarse de que el frame de Categorias se haya inicializado
        if Categorias in self.frames:
            self.frames[Categorias].cargar_categoria()
            print("Cargando categorías al mostrar el frame.") # Depuración
        else:
            print("Error: El frame Categorias no está disponible para cargar datos.")

    def pedidos(self):
        self.show_frames(Pedidos)

    def proveedor(self):
        self.show_frames(Proveedor)

    def informacion(self):
        self.show_frames(Informacion)

    def widgets(self):
        frame2 = tk.Frame(self)
        frame2.place(x=0, y=0, width=1100, height=40)

        self.btn_ventas = Button(frame2, fg="black", text="Ventas", font="sans 16 bold", command=self.ventas)
        self.btn_ventas.place(x=0, y=0, width=184, height=40)

        self.btn_inventario = Button(frame2, fg="black", text="Inventario", font="sans 16 bold", command=self.inventario)
        self.btn_inventario.place(x=184, y=0, width=184, height=40)

        self.btn_categorias = Button(frame2, fg="black", text="Categorias", font="sans 16 bold", command=self.categorias)
        self.btn_categorias.place(x=368, y=0, width=184, height=40)

        self.btn_pedidos = Button(frame2, fg="black", text="Pedidos", font="sans 16 bold", command=self.pedidos)
        self.btn_pedidos.place(x=552, y=0, width=184, height=40)

        self.btn_proveedores = Button(frame2, fg="black", text="Proveedores", font="sans 16 bold", command=self.proveedor)
        self.btn_proveedores.place(x=736, y=0, width=184, height=40)

        self.btn_informacion = Button(frame2, fg="black", text="Informacion", font="sans 16 bold", command=self.informacion)
        self.btn_informacion.place(x=920, y=0, width=180, height=40)

        self.buttons = [self.btn_ventas, self.btn_inventario, self.btn_categorias, self.btn_pedidos, self.btn_proveedores, self.btn_informacion]