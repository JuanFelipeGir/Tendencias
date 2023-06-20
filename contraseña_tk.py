import random
import tkinter as tk
elementos=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',
           '~','@','#','_','^','*','%','/','.','+',':',';','=']

def generar_contraseña(cant):
    tam=range(cant)
    contrasena=[random.choice(elementos) for i in tam]
    contra_label=contrasena

def solicitar_exten():
    cant=int(cant_entry.get())



root = tk.Tk()
root.title("Generador de contraseñas")
root.geometry("300x200")    

titulo_label=tk.Label(root, text="Generador de contraseñas automático")
cant_label=tk.Label(root, text="Ingrese la cantidad")
cant_entry=tk.Entry(root)
cant_button=tk.Button(root,text="Aceptar cantidad",command=solicitar_exten)
convertir_botton=tk.Button(root,text="Generar contraseña",command=generar_contraseña)
contrasena_label=tk.Label(root,text="La contraseña es:")
contra_label=tk.Label(root,generar_contraseña())

root.mainloop()