loteria=int=[]
con=0
while con<=5:
    loteria.append(input(print("ingrese los numeros de la loteeria")))
    con+=1 
else:
    print("Ya se han ingresado todos los numeros")
    loteria.sort()
print(f"Los numeros son:{loteria}") 
