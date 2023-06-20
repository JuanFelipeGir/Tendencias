libro=input(print("Ingrese el valor del libro"))
id=int=input(print("Ingrese el id del libro"))

try:
    archivo=open("prueba.txt","W")
    archivo.write("Nombre del libro:",nombre,"\n")
    archivo.write("ID:",id,"\n")

    archivo.write("Adios")
except Exception as e:
    print(e)
finally:a
