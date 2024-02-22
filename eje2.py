#programa que permita gestionar un prestamo teniendo en cuenta lo siguiente:
#cliente : nombre , contacto
#prestamo: ? - plazo: ? (6(5%)), (12(10%)), (24(15%),(36(20%) meses)
#capacidad de descuento: salario * 0.60
import os
var_nombreStr = input('nombre ->')
var_contactoStr = input ( 'contacto->')
var_salarioFlt = float (input('salario ->'))
var_plazoInt = int(input('- - plazo - -  /n/n1. 6meses/n2. 12 meses/n3. 24 meses /n4. 36 meses /n ->'))
var_capacidad_descuentoFlt = var_salarioFlt * 0.60
var_montoFlt = float(input('monto a prestar ->'))
if var_plazoInt == 1:
    var_interesFlt  = var_montoFlt * 0.05
    var_porcentajeStr = '5%'
    var_opcionInt = 6
if var_plazoInt == 2:
    var_interesFlt = var_montoFlt * 0.10
    var_porcentajeStr = '10%'
    var_opcionInt = 12
if var_plazoInt == 3:
    var_interesFlt = var_montoFlt * 0.15
    var_porcentajeStr = '15%'
    var_opcionInt = 24
if var_plazoInt == 4:
    var_interesFlt = var_montoFlt * 0.20
    var_porcentajeStr = '20%'
    var_opcionInt = 36

var_totalprestamoFlt = var_montoFlt + var_interesFlt
var_cuota = var_totalprestamoFlt / var_opcionInt
os.system('cls')

print('<<<<<< REPORTE DE CREDITO>>>>>>>>>>>')
print('nombre del cliente...................',var_nombreStr)
print('contacto .............................',var_contactoStr)
print('salario..............................', var_salarioFlt)
print('capacidad de descuento................',var_capacidad_descuentoFlt)
print('monto solicitado......................', var_montoFlt)
print('interes................................', var_interesFlt)
print('plazo.................................', var_opcionInt)
print('porcentaje de interes..................',var_porcentajeStr)
print('cuota..................................',var_cuota)
print('total a pagar..........................', var_totalprestamoFlt)

if var_cuota <= var_capacidad_descuentoFlt:
    print('tu cuota ha sido aprobada')
else:
    print('tu credito ha sido rechazado')