import random
import tkinter as tk


elementos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '~', '@', '#', '_', '^', '*', '%', '/', '.', '+', ':', ';', '=']


def generar_contraseña(cant):
    cant = int(cant_entry.get())
    if cant >= 8:
        contrasena = ''.join(random.choice(elementos) for i in range(cant))
        contra_label.config(text=contrasena)
        with open('log.txt', 'a') as f:
         f.write(contrasena + '\n')  # Agregar la contraseña generada en una nueva línea al final del archivo


def solicitar_exten():
    cant = int(cant_entry.get())


root = tk.Tk()
root.title("Generador de contraseñas")
root.geometry("300x200")

titulo_label = tk.Label(root, text="Generador de contraseñas automático")
cant_label = tk.Label(root, text="Ingrese la cantidad")
cant_entry = tk.Entry(root)
cant_button = tk.Button(root, text="Aceptar cantidad", command=solicitar_exten)
convertir_botton = tk.Button(root, text="Generar contraseña", command=lambda: generar_contraseña(int(cant_entry.get())))
contrasena_label = tk.Label(root, text="La contraseña es:")
contra_label = tk.Label(root, text="", font=('Arial', 12), fg='blue')

titulo_label.pack(pady=5)
cant_label.pack()
cant_entry.pack()
cant_button.pack(pady=5)
convertir_botton.pack(pady=5)
contrasena_label.pack()
contra_label.pack(pady=5)

root.mainloop()