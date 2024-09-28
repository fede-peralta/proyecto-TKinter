# GRUPO N°: 14 
# INTEGRANTES : Julieta blanco, Cristian Ivan Soto, Alberto Alejandro Diaz, Federico Peralta, Daiana Marchek
# Mini Proyecto: Regristro de Concesionaria



import os
import datetime
import tkinter as tk
from tkinter import messagebox

anio_actual = datetime.datetime.now().year
Stock = []

def f_mantenimiento():
    mant = input('corresponde mantenimiento (si/no): ').lower()
    return mant == 'si'

def validar_anio_modelo(modelo):
    if modelo > anio_actual:
        return False
    elif (anio_actual - modelo) <= 10:
        return True
    else:
        return False

# Función para agregar un vehículo
def agregar_vehiculo(patente, n_chasis, marca, modelo, modelo_comercial, tipo_vehiculo, color, kilometraje, motor, caracteristicas):
    vehiculo = {
        'patente': patente,
        'n_chasis': n_chasis,
        'marca': marca,
        'modelo': int(modelo),
        'modelo_comercial': modelo_comercial,
        'tipo_vehiculo': tipo_vehiculo,
        'color': color,
        'kilometraje': int(kilometraje),
        'motor': motor,
        'caracteristicas': caracteristicas,
        'mantenimiento': True,  # Este valor se puede ajustar
        'estado': 'Disponible'
    }
    Stock.append(vehiculo)
    messagebox.showinfo("Éxito", "Vehículo agregado correctamente")

# Función para listar los vehículos en el stock
def listar_stock():
    lista.delete(0, tk.END)
    if not Stock:
        lista.insert(tk.END, "No hay vehículos en el stock.")
    else:
        for vehiculo in Stock:
            lista.insert(tk.END, f"Patente: {vehiculo['patente']}, Marca: {vehiculo['marca']}, Modelo: {vehiculo['modelo']}")

# Función para buscar un vehículo por patente
def buscar_vehiculo(patente):
    lista.delete(0, tk.END)
    encontrado = False
    for vehiculo in Stock:
        if vehiculo['patente'] == patente:
            lista.insert(tk.END, f"Vehículo encontrado: Patente: {vehiculo['patente']}")
            lista.insert(tk.END, f"Marca: {vehiculo['marca']}, Modelo: {vehiculo['modelo']}")
            lista.insert(tk.END, f"Color: {vehiculo['color']}, Kilometraje: {vehiculo['kilometraje']}")
            lista.insert(tk.END, f"Motor: {vehiculo['motor']}, Características: {vehiculo['caracteristicas']}")
            encontrado = True
            break
    if not encontrado:
        messagebox.showwarning("No encontrado", f"No se encontró ningún vehículo con la patente {patente}")

# Función para eliminar un vehículo por patente
def eliminar_vehiculo(patente):
    global Stock
    for vehiculo in Stock:
        if vehiculo['patente'] == patente:
            Stock = [v for v in Stock if v['patente'] != patente]
            messagebox.showinfo("Éxito", f"Vehículo con patente {patente} eliminado correctamente")
            listar_stock()  # Actualizamos la lista después de eliminar
            return
    messagebox.showwarning("No encontrado", f"No se encontró ningún vehículo con la patente {patente}")

# Interfaz gráfica con Tkinter
ventana = tk.Tk()
ventana.title("Gestión de Vehículos")

# Labels y campos de entrada para el formulario
tk.Label(ventana, text="Patente").grid(row=0, column=0)
entry_patente = tk.Entry(ventana)
entry_patente.grid(row=0, column=1)

tk.Label(ventana, text="Número de Chasis").grid(row=1, column=0)
entry_chasis = tk.Entry(ventana)
entry_chasis.grid(row=1, column=1)

tk.Label(ventana, text="Marca").grid(row=2, column=0)
entry_marca = tk.Entry(ventana)
entry_marca.grid(row=2, column=1)

tk.Label(ventana, text="Modelo (Año)").grid(row=3, column=0)
entry_modelo = tk.Entry(ventana)
entry_modelo.grid(row=3, column=1)

tk.Label(ventana, text="Modelo Comercial").grid(row=4, column=0)
entry_modelo_comercial = tk.Entry(ventana)
entry_modelo_comercial.grid(row=4, column=1)

tk.Label(ventana, text="Tipo de Vehículo").grid(row=5, column=0)
entry_tipo = tk.Entry(ventana)
entry_tipo.grid(row=5, column=1)

tk.Label(ventana, text="Color").grid(row=6, column=0)
entry_color = tk.Entry(ventana)
entry_color.grid(row=6, column=1)

tk.Label(ventana, text="Kilometraje").grid(row=7, column=0)
entry_kilometraje = tk.Entry(ventana)
entry_kilometraje.grid(row=7, column=1)

tk.Label(ventana, text="Motor").grid(row=8, column=0)
entry_motor = tk.Entry(ventana)
entry_motor.grid(row=8, column=1)

tk.Label(ventana, text="Características").grid(row=9, column=0)
entry_caracteristicas = tk.Entry(ventana)
entry_caracteristicas.grid(row=9, column=1)

# Botón para agregar vehículo
btn_agregar = tk.Button(ventana, text="Agregar Vehículo", command=lambda: agregar_vehiculo(
    entry_patente.get(), entry_chasis.get(), entry_marca.get(), entry_modelo.get(), 
    entry_modelo_comercial.get(), entry_tipo.get(), entry_color.get(), 
    entry_kilometraje.get(), entry_motor.get(), entry_caracteristicas.get()))
btn_agregar.grid(row=10, column=0, columnspan=2)

# Lista para mostrar el stock de vehículos
lista = tk.Listbox(ventana, width=80, height=10)
lista.grid(row=11, column=0, columnspan=2)

# Botón para listar el stock
btn_listar = tk.Button(ventana, text="Listar Stock", command=listar_stock)
btn_listar.grid(row=12, column=0, columnspan=2)

# Campo y botón para buscar vehículo por patente
tk.Label(ventana, text="Buscar por patente").grid(row=13, column=0)
entry_buscar_patente = tk.Entry(ventana)
entry_buscar_patente.grid(row=13, column=1)

btn_buscar = tk.Button(ventana, text="Buscar Vehículo", command=lambda: buscar_vehiculo(entry_buscar_patente.get()))
btn_buscar.grid(row=14, column=0, columnspan=2)

# Campo y botón para eliminar vehículo por patente
tk.Label(ventana, text="Eliminar por patente").grid(row=15, column=0)
entry_eliminar_patente = tk.Entry(ventana)
entry_eliminar_patente.grid(row=15, column=1)

btn_eliminar = tk.Button(ventana, text="Eliminar Vehículo", command=lambda: eliminar_vehiculo(entry_eliminar_patente.get()))
btn_eliminar.grid(row=16, column=0, columnspan=2)

# Ejecutar la aplicación
ventana.mainloop() 