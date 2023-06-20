mesing=int(input("Ingrese un mes"))
'''3,4,5,6 primavera
7,8,9 verano
10,11 otoño
12,1,2''' 
if mesing==3 or mesing==4 or mesing==5 or mesing==6:
    print("Estas en primavera")
elif mesing==7 or mesing==8 or mesing==9:
    print("Estamos en verano")
elif mesing==10 or mesing==11:
    print("Estamos en otoño")
elif mesing==12 or mesing==1 or mesing==2:
    print("Estamos en invierno")                
else:
    print("Mes no ingresado")
