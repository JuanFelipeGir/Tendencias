peso=float(input(print("Ingrese el peso")))
estat=float(input(print("Ingrese la estatura en metros")))

imc=round(peso/(estat**2),2)   
print(f"Tu índice de masa corporal es: {imc}")