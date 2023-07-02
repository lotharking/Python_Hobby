class Banco():
    id: int = 1
    nombre: str = "banco1"

class Usuario():
    nombre = "camilo"
    cuenta = 1111
    banco_id = Banco.id

class Cuenta():
    id = 1
    numero = Usuario.cuenta
    banco = Banco.id
    saldo = 1000

class Usuario2():
    nombre = "arturo"
    cuenta = 2222
    banco_id = Banco.id

class Cuenta2():
    id = 1
    numero = Usuario.cuenta
    banco = Banco.id
    saldo = 2000

def ConsultarSaldo():
    name = "camilo"
    if name == Usuario.nombre:
        if Usuario.banco_id == Cuenta.banco:
            print("Su saldo actual es: "+ str(Cuenta.saldo))
        else:
            raise Exception("el usuario no tiene una cuenta creada")
    else:
        raise Exception("usuario no encontrado")

def ConsignarCuenta():
    name = "camilo"
    cuenta = 1111
    consignacion = 500
    if name == Usuario.nombre:
        if cuenta == Usuario.cuenta:
            saldo = Cuenta.saldo
            saldo += consignacion
            Cuenta.saldo = saldo
            print("su nuevo saldo es:" + str(Cuenta.saldo))
        else:
            raise Exception("Cuenta erronea por favor valide")
    else:
        raise Exception("usuario no encontrado")

def RetirarDineroCuenta():
    name = "camilo"
    cuenta = 1111
    consignacion = 200
    if name == Usuario.nombre:
        if cuenta == Usuario.cuenta:
            saldo = Cuenta.saldo
            saldo -= consignacion
            if saldo >= 0:
                Cuenta.saldo = saldo
                print("su nuevo saldo es:" + str(Cuenta.saldo))
            else:
                raise Exception("No cuenta con fondos suficientes para realizar la operacion")
        else:
            raise Exception("Cuenta erronea por favor valide")
    else:
        raise Exception("usuario no encontrado")
    
# def Transferencia():
#     name="arturo"
#     cuenta = 2222
#     valor = 200
#     cuentadestino = 1111
#     if name == Usuario2.nombre:
#         if cuenta == Usuario2.cuenta:
#             saldoOrigen = Cuenta2.saldo
#             saldoOrigen -= valor
#             if C
#             if cuentadestino == Usuario.cuenta:

#         else:
#             raise Exception("Cuenta erronea por favor valide")
#     else:
#         raise Exception("usuario no encontrado")


ConsultarSaldo()
ConsignarCuenta()
RetirarDineroCuenta()