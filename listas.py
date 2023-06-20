
'''
vehiculo=["moto","carro","avión"]
numero=[1,2,3,4,5,6,7]
logicos=[True,False,True]
variados=[True,"carro",1]

print(vehiculo,"\n",numero,"\n",logicos,"\n")
print(variados)
'''
nombre=["pablito","clavó","un","clavito"]
print(nombre[0])
print(nombre[-1])
print(nombre[0:2])
print(f'{nombre[:3]}')
print(f'{nombre[1:]}')
nombre[3]="sandra"
for nombre in nombre:
    print(nombre)
else:
    print("No existen mas nombres en la lista")



nombres=["cristian","Juan","Camila","Andres"]
print(len(nombres))

nombres.append("Lorenza")
nombres.insert(1,"Vanessa")
print (nombres)
nombres.remove("Lorenza")
print(nombres)
nombres.pop(3)
print(nombres)
del nombres[0]
print(nombres)
nombres.clear
