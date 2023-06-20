import sys
class Persona:
    def __init__(self, nombre, apellido, numeroDocumento, telefono, usuario, clave):
        self.nombre = nombre
        self.apellido = apellido
        self.numeroDocumento = numeroDocumento
        self.telefono = telefono
        self.usuario = usuario
        self.clave = clave


class Cuenta:
    def __init__(self, numeroCuenta, propietario, estado, tipoCuenta, balance):
        self.numeroCuenta = numeroCuenta
        self.propietario = propietario
        self.estado = estado
        self.tipoCuenta = tipoCuenta
        self.balance = balance

    def agregar_fondos(self, monto):
        if self.estado == "Abierta":
            self.balance += monto
            print("Se han agregado {} fondos a su cuenta. El nuevo balance es de {}.".format(monto, self.balance))
        else:
            print("No se pueden agregar fondos a una cuenta cerrada.")

    def retirar_fondos(self, monto):
        if self.estado == "Abierta":
            if self.balance >= monto:
                self.balance -= monto
                print("Se han retirado {} fondos de su cuenta. El nuevo balance es de {}.".format(monto, self.balance))
            else:
                print("No hay suficientes fondos en su cuenta para retirar {}.".format(monto))
        else:
            print("No se pueden retirar fondos de una cuenta cerrada.")

    def cerrar_cuenta(self):
        if self.estado == "Abierta":
            self.estado = "Cerrada"
            print("La cuenta ha sido cerrada.")
        else:
            print("La cuenta ya está cerrada.")


class Banco:
    def __init__(self):
        self.propietarios = []
        self.cuentas = []

    def registrar_propietario(self, nombre, apellido, numeroDocumento, telefono, usuario, clave):
        propietario = Persona(nombre, apellido, numeroDocumento, telefono, usuario, clave)
        self.propietarios.append(propietario)
        print("Se ha registrado el propietario {} {} con usuario {}.".format(nombre, apellido, usuario))

    def registrar_cuenta(self, propietario, tipoCuenta, balance):
        cuenta_existente = False
        for cuenta in self.cuentas:
            if cuenta.propietario == propietario:
                cuenta_existente = True
                break
        if not cuenta_existente:
            numeroCuenta = str(len(self.cuentas) + 1).zfill(5)
            cuenta = Cuenta(numeroCuenta, propietario, "Abierta", tipoCuenta, balance)
            self.cuentas.append(cuenta)
            print("Se ha registrado la cuenta {} del propietario {} {} con un balance inicial de {}.".format(
                numeroCuenta, propietario.nombre, propietario.apellido, balance))
        else:
            print("El propietario ya tiene una cuenta registrada.")

    def iniciar_sesion(self, usuario, clave):
        for propietario in self.propietarios:
            if propietario.usuario == usuario and propietario.clave == clave:
                return propietario
        print("El usuario o clave no son válidos.")
        return None


def menu():
    print("Seleccione una opción:")
    print("1. Añadir fondos a su cuenta.")
    print("2. Retirar fondos de su cuenta.")
    print("3. Cerrar cuenta.")
    print("4. Cerrar sesión.")
    opcion = input()
    return opcion


banco = Banco()
while True:
    print("Bienvenido al banco.")
    print("1. Registrar propietario.")
    print("2. Registrar cuenta.")
    print("3. Iniciar sesión.")
    print("4. Salir.")
    opcion = input()

    if opcion == "1":
        print("Ingrese los datos del propietario:")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        numeroDocumento = input("Número de documento: ")
        telefono = input("Teléfono: ")
        usuario = input("Usuario: ")
        clave = input("Clave: ")
        banco.registrar_propietario(nombre, apellido, numeroDocumento, telefono, usuario, clave)

    elif opcion == "2":
        print("Ingrese los datos de la cuenta:")
        propietario_usuario = input("Usuario del propietario: ")
        propietario_clave = input("Clave del propietario: ")
        propietario = banco.iniciar_sesion(propietario_usuario, propietario_clave)
        if propietario is not None:
            tipoCuenta = input("Tipo de cuenta (ahorros o corriente): ")
            balance = float(input("Balance inicial: "))
            banco.registrar_cuenta(propietario, tipoCuenta, balance)

    elif opcion == "3":
        print("Ingrese sus credenciales para iniciar sesión:")
        usuario = input("Usuario: ")
        clave = input("Clave: ")
        propietario = banco.iniciar_sesion(usuario, clave)
        if propietario is not None:
            while True:
                opcion = menu()
                if opcion == "1":
                    numeroCuenta = input("Ingrese el número de cuenta: ")
                    cuenta = None
                    for c in banco.cuentas:
                        if c.numeroCuenta == numeroCuenta and c.propietario == propietario:
                            cuenta = c
                            break
                    if cuenta is not None:
                        monto = float(input("Ingrese el monto a agregar: "))
                        cuenta.agregar_fondos(monto)
                    else:
                        print("No se encontró la cuenta.")

                elif opcion == "2":
                    numeroCuenta = input("Ingrese el número de cuenta: ")
                    cuenta = None
                    for c in banco.cuentas:
                        if c.numeroCuenta == numeroCuenta and c.propietario == propietario:
                            cuenta = c
                            break
                    if cuenta is not None:
                        monto = float(input("Ingrese el monto a retirar: "))
                        cuenta.retirar_fondos(monto)
                    else:
                        print("No se encontró la cuenta.")

                elif opcion == "3":
                    numeroCuenta = input("Ingrese el número de cuenta: ")
                    cuenta = None
                    for c in banco.cuentas:
                        if c.numeroCuenta == numeroCuenta and c.propietario == propietario:
                            cuenta = c
                            break
                    if cuenta is not None:
                        cuenta.cerrar_cuenta()
                    else:
                        print("No se encontró la cuenta.")

                if opcion == "4":
                    sys.exit()
                    break
                