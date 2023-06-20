import tkinter as tk
from tkinter import ttk, messagebox

def celsius_fahrenheit():
    celsius=float(celsius_entry.get())
    fahrenheit=round((celsius* 9/5) + 32, 1)
    fahrenheit_label.config(text=f"{fahrenheit} °F")

def fahrenheit_celsius(fahrenheit):
    celsius=round((fahrenheit - 32) * 5/9, 1)
    celsius_label.config(text=f"{celsius}°C")

def convertir_celsius_fahrenheit():
    celsius_fahrenheit()
    celsius_fahrenheit(float(fahrenheit_entry.get()))

def convertir_fahrenheit_celsius():
    fahrenheit_celsius(float(fahrenheit_entry.get()))
    celsius_fahrenheit()

def exportar():
    celsius=float(celsius_entry.get())
    fahrenheit=round((celsius* 9/5) + 32, 1)
    celsius2 = round((float(fahrenheit_entry.get()) - 32) * 5/9, 1)
    with open("convertidor_grados.txt","W") as file:
        file.write(f"Grados celsius{celsius}°C\n")
        file.write(f"Grados fahrenheit{float(fahrenheit_entry.get())}°F\n")
        file.write(f"Grados Fahrenheit a Celsius: {celsius2}°C\n")
        file.write(f"Grados celsius a Fahrenheit{fahrenheit}°F\n")
        file.close
    tk.messagebox.showinfo("Datos exportados\n", "Se han exportado los datos")

    ventana=tk.Tk()
    ventana.title("Convertidor de Temperatura")
    ventana.geometry("600x400")

    Convertir_Fahrenheit=ttk.Button(ventana,text="Convertir a Celsius", command=convertir_fahrenheit_celsius())
    Convertir_Celsius=ttk.Button(ventana,text="Convertir a Fahrenheit", command=convertir_celsius_fahrenheit())
    Exportar=ttk.Button(ventana,text="Exportar")
    celsius_label=tk.Label(ventana,text="Grados celsius")
    celsius_entry=tk.Entry(ventana)
    fahrenheit_label=tk.Label(ventana,text="Grados Fahrenheit")
    fahrenheit_entry=tk.Entry(ventana)

    celsius_label.grid(row=0, column=0)
    celsius_entry.grid(row=0, column=1)
    Convertir_Celsius.grid(row=0,column=2,pady=10)
    fahrenheit_label.grid(row=1,column=0)
    fahrenheit_entry.grid(row=1,column=1)
    Convertir_Celsius.grid(row=1,column=2,pady=10)
    Exportar.grid(row=2,column=1, columnspan=2)

    ventana.mainloop()