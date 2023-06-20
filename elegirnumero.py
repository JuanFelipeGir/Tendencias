con=int(input(print("¿Cuantos numeros desea ingresar?")))
numeros=[]
num=range(con)

for num in num:
    numeros.append(input(print(f"ingrese el numero: ")))
    numeros.sort()

print(f"El numero mas pequeño es: {numeros[0]}")
print(f"El numero mas mas grande es: {numeros[-1]}")




