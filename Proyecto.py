numero=int(input("Proporciona un valor entre 1 y 3"))
numeroTexto=''
if numero ==1:
    numeroTexto="Numero uno"
elif numero==2:
    numeroTexto="Numero dos"
elif numero==3:
    numeroTexto="Numero tres"
else:
    numeroTexto="Valor no fuera de rangos"
print(f"numero proporcionado:{numero}-{numeroTexto}")

