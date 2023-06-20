notaing=int(input("Ingrese una nota"))

if notaing>=9 and notaing<=10:
    print("Tu nota es una A")
elif notaing==8:
    print("tu nota es una B")
elif notaing==7:
    print("Tu nota| es C")
elif notaing==6:
    print("Tu nota es una D")
elif notaing<6:
    print("Tu nota es una F")                    
else:
    print("El rango de calificación ingresado es incorrecto")
