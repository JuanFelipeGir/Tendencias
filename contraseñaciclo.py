
print("Hola, Por favor ingrese la contraseña")
contra=input(print("Ingrese la contraseña"))

print("Por favor valide su contraseña")
contra2=input(print("Ingrese nuevamente su contraseña"))
opc=True
while opc:   
    if contra2== contra:
        print("La contaerseña es correcta")
        opc=False
    else:
        contra2=input(print("contraseña incorrecta ingrese nuevamente su contraseña"))

