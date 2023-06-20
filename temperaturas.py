con=int(input(print("¿Cuantas temperaturas desea ingresar")))
temperatura=[]
num=range(con)
ciudad=1
for num in num:
    print("Ingrese las temperaturas")
    temperatura.append(input(print(f"ingrese las temperaturas de la ciudad {ciudad}")))
    ciudad=ciudad+1
    print(temperatura)

suma=0
valor=int
for valor in temperatura:
    suma=suma+temperatura[valor]

print(f"La suma es {suma}")

cantidad_elementos = len(temperatura)
promedio = suma / cantidad_elementos
print(f"El promedio es {promedio}")


