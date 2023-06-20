

    '''try: 
    archivo=open('prueba.txt', 'w')
    archivo.write('si te he fallado te pido perdon de la unica forma que se\n')
    archivo.write('╰(*°▽°*)╯')
except Exception as e:
    print(e)
finally:
    archivo.close()'''

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