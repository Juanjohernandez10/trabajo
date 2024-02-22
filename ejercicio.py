
cons_existenciaInt = 5
var_cantidadInt = int (input('ingrese la cantidad de videojuego a presentar'))


if var_cantidadInt <= 0:
    print('la cantidad de videojuegos debe ser mayor a 0')
else:
    if var_cantidadInt <= cons_existenciaInt:
        print('tu prestamo ha sido aprobado')
        print('existencias actual:', (cons_existenciaInt - var_cantidadInt))
        enter = input('presione < ENTER > para continuar')
    else:
        print('no tenemos la cantidad de vidojuegos disponibles')