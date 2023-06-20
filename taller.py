import tkinter as tk

def celsius_fahrenheit():
    celsius = float(celsius_entry.get())
    fahrenheit = round((celsius * 9/5) + 32, 1)
    fahrenheit_label.config(text=f"{fahrenheit}°F")

def fahrenheit_celsius(fahrenheit):
    celsius = round((fahrenheit - 32) * 5/9, 1)
    celsius_label.config(text=f"{celsius}°C")

def convertir_celsius_fahrenheit():
    celsius_fahrenheit()
    fahrenheit_celsius(float(fahrenheit_entry.get()))

def convertir_fahrenheit_celsius():
    fahrenheit_celsius(float(fahrenheit_entry.get()))
    celsius_fahrenheit()

def exportararchivo():
    celsius = float(celsius_entry.get())
    fahrenheit = round((celsius * 9/5) + 32, 1)
    celsius2 = round((float(fahrenheit_entry.get()) - 32) * 5/9, 1)
    with open("covertidor_grados.txt", "w") as file:
        file.write(f"Grados Celsius: {celsius}°C\n")
        file.write(f"Grados Fahrenheit: {float(fahrenheit_entry.get())}°F\n")
        file.write(f"Grados Fahrenheit a Celsius: {celsius2}°C\n")
        file.write(f"Grados Celsius a Fahrenheit: {fahrenheit}°F\n")
    tk.messagebox.showinfo("Datos exportados", "Los datos se han exportado correctamente.")

# Configurar la ventana principal
root = tk.Tk()
root.title("Conversor de grados")
root.geometry("300x200")

# Crear los elementos de la interfaz gráfica
celsius_label = tk.Label(root, text="Grados Celsius:")
celsius_entry = tk.Entry(root)
fahrenheit_label = tk.Label(root, text="Grados Fahrenheit:")
fahrenheit_entry = tk.Entry(root)
celsius_button = tk.Button(root, text="Convertir a Fahrenheit", command=convertir_celsius_fahrenheit)
fahrenheit_button = tk.Button(root, text="Convertir a Celsius", command=convertir_fahrenheit_celsius)
export_button = tk.Button(root, text="Exportar", command=exportararchivo)

# Ubicar los elementos en la interfaz gráfica
celsius_label.grid(row=0, column=0)
celsius_entry.grid(row=0, column=1)
fahrenheit_label.grid(row=1, column=0)
fahrenheit_entry.grid(row=1, column=1)
celsius_button.grid(row=2, column=0, pady=10)
fahrenheit_button.grid(row=2, column=1, pady=10)
export_button.grid(row=3, column=0, columnspan=2)

# Iniciar la aplicación
root.mainloop()