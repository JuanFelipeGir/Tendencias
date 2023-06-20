import tkinter as tk
from tkinter import ttk, messagebox, Menu   
from urllib.request import urlopen
from setuptools import Command


def salir():
    ventana.quit()
    ventana.destroy()
    SystemExit()

def evento_click():
    print('ay we, si le espichaste')
    boton1.config(text='boton espichado')
    boton2=ttk.Button(ventana, text='no le des aquí', command=evento_click2)
    boton2.grid(row=0, column=1)
def evento_click2():
    print('te quero (/ω＼)')
    
def evento_entrar():
    mensaje1='Datos actualizados'
    messagebox.showinfo('mensaje informativo ', mensaje1)
    boton3.config(text='enviado')
    etiqueta1=tk.Label(ventana, text=entrada1.get())
    etiqueta1.grid(row=2, column=0, columnspan=2)
    print(entrada1.get())

ventana=tk.Tk()
ventana.geometry('600x400')
ventana.title('que lok')

boton1=ttk.Button(ventana, text='espichale click', command=evento_click)
boton1.grid(row=0, column=0, padx=69, pady=69)

entrada1=ttk.Entry(ventana, width=30)
entrada1.grid(row=1, column=0)
boton3=ttk.Button(ventana, text='entrar', command=evento_entrar)
boton3.grid(row=1, column=1)

def menu():
    menup=Menu(ventana)
    submenu=Menu(menup, tearoff=0)
    submenu.add_command(label='Nuevo')
    submenu.add_command(label='Ayuda')
    submenu.add_command(label='Salir', command=salir)
    submenuayuda=Menu(menup, tearoff=0)
    menup.add_cascade(menu=submenu, label='Ayuda')
    menup.add_cascade(menu=submenuayuda, label='Archivo')

    ventana.config(menu=menup)


mensajerror='informacion invalida'
messagebox.showerror('mensaje erroneo ',mensajerror + ' error' )



mensaje2='advertencia'
messagebox.showwarning('Alerta ', mensaje2)

menu()


ventana.mainloop()