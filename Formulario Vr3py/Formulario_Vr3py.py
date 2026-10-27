
import mysql.connector
import tkinter as tk
from tkinter import messagebox


def guardar():
  nombre = txt_nombre.get().strip()
  apellidos = txt_apellido.get().strip()
  telefono = txt_telefono.get().strip()
  edad = txt_edad.get().strip()
  estatura = txt_estatura.get().strip()
  genero = var_genero.get()

  if nombre == "" or apellidos == "":
    messagebox.showwarning("Atencion", "Ingresa al menos nombre y apellido.")
    return

  try:
    conexion = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="registrousuariospa",
    )
    cursor = conexion.cursor()

    sql = "INSERT INTO usuarios (Nombre, Apellidos, Telefono, Estatura, Edad, Genero) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (
        nombre,
        apellidos,
        int(telefono),
        float(estatura),
        int(edad),
        genero,
    )

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo(
        "Exito", "Registro guardado correctamente en la base de datos."
    )
    limpiar()

    cursor.close()
    conexion.close()

  except Exception as error:
    messagebox.showerror("Error", "Error al guardar: " + str(error))


def limpiar():
  txt_nombre.delete(0, tk.END)
  txt_apellido.delete(0, tk.END)
  txt_telefono.delete(0, tk.END)
  txt_edad.delete(0, tk.END)
  txt_estatura.delete(0, tk.END)
  var_genero.set("Otro")
  txt_nombre.focus()


ventana = tk.Tk()
ventana.title("Practica 04 - Registro de Datos")
ventana.geometry("500x310")

lbl_nombre = tk.Label(ventana, text="Nombres:")
lbl_nombre.place(x=30, y=30)
txt_nombre = tk.Entry(ventana)
txt_nombre.place(x=120, y=30, width=170)

lbl_apellido = tk.Label(ventana, text="Apellidos:")
lbl_apellido.place(x=30, y=70)
txt_apellido = tk.Entry(ventana)
txt_apellido.place(x=120, y=70, width=170)

lbl_telefono = tk.Label(ventana, text="Telefono:")
lbl_telefono.place(x=30, y=110)
txt_telefono = tk.Entry(ventana)
txt_telefono.place(x=120, y=110, width=170)

lbl_edad = tk.Label(ventana, text="Edad:")
lbl_edad.place(x=30, y=150)
txt_edad = tk.Entry(ventana)
txt_edad.place(x=120, y=150, width=170)

lbl_estatura = tk.Label(ventana, text="Estatura:")
lbl_estatura.place(x=30, y=190)
txt_estatura = tk.Entry(ventana)
txt_estatura.place(x=120, y=190, width=170)

gb_genero = tk.LabelFrame(ventana, text="Genero")
gb_genero.place(x=320, y=25, width=140, height=130)

var_genero = tk.StringVar(value="Otro")

rb_masculino = tk.Radiobutton(
    gb_genero, text="Masculino", variable=var_genero, value="Hombre"
)
rb_masculino.place(x=10, y=10)

rb_femenino = tk.Radiobutton(
    gb_genero, text="Femenino", variable=var_genero, value="Mujer"
)
rb_femenino.place(x=10, y=35)

rb_otro = tk.Radiobutton(
    gb_genero, text="Otro", variable=var_genero, value="Otro"
)
rb_otro.place(x=10, y=60)

btn_guardar = tk.Button(ventana, text="Guardar", command=guardar, width=10)
btn_guardar.place(x=120, y=240)

btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar, width=10)
btn_limpiar.place(x=220, y=240)

ventana.mainloop()