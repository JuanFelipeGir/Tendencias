'''
def mi_putafncion():
    print("Saludos gentecilla de youtube")
mi_putafncion()

def nombres(nombres, apellidos):
    print(f"{nombres}{apellidos}")
nombres("Juan", "Giraldo")

def suma(a,b):
    return a+b
resultado=suma(5,5)


def nombres(*nombres):
    for nombre in nombres:
        print(nombre)
nombres("juan","carlota","pedro")
nombres("pepes")

print(nombres)
'''

def sumas():
    a=int(input("Ingrese el primer numero"))
    b=int(input("ingrese el segundo numero"))
    c=int(input("ingrese el tercer numero"))
    d=int(input("ingrese el ultimo numero"))
    print(a+b+c+d)
sumas()