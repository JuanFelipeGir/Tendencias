'''
id=int(input("ingrese el id del libro"))
lname=input("ingrese el nombre del libro")
value=float(input("ingrese el precio del libro"))

if value>= 100.000:
    print(f'{id} \n {lname} \n {value:.3f}')
    print("el envio del libro es gratis")
else:
    print(f'{id} \n {lname} \n {value:.3f}')
    print("el envio del libro no es gratis")
'''

'''
condicion = str(input('ingrese condicion'))
if condicion == 'True':
    print('condicion verdadera')
elif condicion == 'False':
    print('condicion falsa')
else:
    print('condicion no reconocida')
'''
'''
try: 
    archivo=open('prueba.txt', 'w')
    archivo.write('si te he fallado te pido perdon de la unica forma que se\n')
    archivo.write('╰(*°▽°*)╯')
except Exception as e:
    print(e)
finally:
    archivo.close()
    '''

ejercicio = f'nombre del libro: regarding sayaka \n IDlibro: 123456 ' \
            f'\n valor: 20.000 \n envio: False'
try:
    livre = open('ejerciciolibro.txt', 'w')
    livre.write(ejercicio)
    livre.write('╰(*°▽°*)╯')
except Exception as e:
    print(e)
finally:
    livre.close()

livre=open(r'C:\ejerciciolibro.txt')
print(livre.read())

archivo2=open(copiar.txt)
archivo2.write(livre.read())

archivo2.close
livre.close