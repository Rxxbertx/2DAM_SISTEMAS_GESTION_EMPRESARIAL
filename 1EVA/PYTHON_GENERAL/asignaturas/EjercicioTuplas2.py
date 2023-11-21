#meses pero la clave se representa con un numero
meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Setiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

#ahora pedimos la fecha al usuario en formato dd/mm/aaaa
fecha = input("Introduce una fecha en formato dd/mm/aaaa: ")

#separamos la fecha en dia, mes y año

dia = int(fecha[:2])
mes = int(fecha[3:5])
año = int(fecha[6:])

#imprimimos la fecha en formato dd de mes de aaaa
print(dia, "de", meses[mes], "de", año)
